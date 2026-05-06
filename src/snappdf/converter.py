"""PDF 页面转图片的转换器模块。

在后台线程中执行 PDF 到图片的转换操作，通过信号报告进度。
"""

from pathlib import Path

from PySide6.QtCore import QSize, QThread, Signal
from PySide6.QtGui import QImage, QImageWriter
from PySide6.QtPdf import QPdfDocument, QPdfDocumentRenderOptions

PDF_POINTS_PER_INCH = 72.0


def get_pdf_page_count(pdf_path: str) -> int:
    """获取 PDF 总页数。"""
    document = QPdfDocument()
    try:
        _load_document(document, pdf_path)
        return document.pageCount()
    finally:
        document.close()


def _load_document(document: QPdfDocument, pdf_path: str) -> None:
    """加载 PDF 文档，失败时抛出易读错误。"""
    error = document.load(pdf_path)
    if error != QPdfDocument.Error.None_:
        raise RuntimeError(f"无法打开 PDF 文件：{_format_pdf_error(error)}")


def _format_pdf_error(error: QPdfDocument.Error) -> str:
    """将 QtPdf 错误枚举转换成适合显示的文本。"""
    messages = {
        QPdfDocument.Error.Unknown: "未知错误",
        QPdfDocument.Error.DataNotYetAvailable: "PDF 数据尚未准备好",
        QPdfDocument.Error.FileNotFound: "文件不存在",
        QPdfDocument.Error.InvalidFileFormat: "PDF 格式无效",
        QPdfDocument.Error.IncorrectPassword: "密码错误",
        QPdfDocument.Error.UnsupportedSecurityScheme: "不支持的 PDF 加密方式",
    }
    return messages.get(error, error.name)


def _page_image_size(document: QPdfDocument, page_num: int, dpi: int) -> QSize:
    """按目标 DPI 计算页面渲染像素尺寸。"""
    point_size = document.pagePointSize(page_num)
    scale = dpi / PDF_POINTS_PER_INCH
    width = max(1, round(point_size.width() * scale))
    height = max(1, round(point_size.height() * scale))
    return QSize(width, height)


def _image_writer_format(ext: str) -> bytes:
    """返回 QImageWriter 使用的图片格式名。"""
    if ext == "jpg":
        return b"jpeg"
    return ext.encode("ascii")


def _save_image(image: QImage, out_path: str, ext: str, quality: int) -> None:
    """保存渲染后的页面图片。"""
    writer = QImageWriter(out_path, _image_writer_format(ext))
    if ext in {"jpg", "jpeg", "webp"}:
        writer.setQuality(quality)

    if not writer.write(image):
        raise RuntimeError(f"保存图片失败：{writer.errorString()}")


class ConvertWorker(QThread):
    """PDF 转图片的工作线程。"""

    progress_changed = Signal(int, int, str)  # (当前页, 总页数, 文件名)
    finished_all = Signal(list)  # 输出文件路径列表
    error_occurred = Signal(str)  # 错误信息

    def __init__(
        self,
        pdf_path: str,
        output_dir: str,
        fmt: str,
        quality: int,
        dpi: int,
        pages: list[int] | None,
    ) -> None:
        """初始化转换工作线程。"""
        super().__init__()
        self._pdf_path = pdf_path
        self._output_dir = output_dir
        self._fmt = fmt
        self._quality = quality
        self._dpi = dpi
        self._pages = pages

    def run(self) -> None:
        """执行 PDF 到图片的转换。"""
        document = QPdfDocument()
        try:
            _load_document(document, self._pdf_path)
            total = document.pageCount()
            target_pages = self._pages if self._pages else list(range(total))
            output_paths: list[str] = []

            options = QPdfDocumentRenderOptions()
            options.setRenderFlags(QPdfDocumentRenderOptions.RenderFlag.Annotations)

            ext = self._fmt.lower()
            for i, page_num in enumerate(target_pages):
                if page_num < 0 or page_num >= total:
                    continue

                image_size = _page_image_size(document, page_num, self._dpi)
                image = document.render(page_num, image_size, options)
                if image.isNull():
                    raise RuntimeError(f"第 {page_num + 1} 页渲染失败")

                out_name = f"{Path(self._pdf_path).stem}_page{page_num + 1}.{ext}"
                out_path = str(Path(self._output_dir) / out_name)
                _save_image(image, out_path, ext, self._quality)

                output_paths.append(out_path)
                self.progress_changed.emit(i + 1, len(target_pages), out_name)

            self.finished_all.emit(output_paths)

        except Exception as e:
            self.error_occurred.emit(f"转换失败：{e}")
        finally:
            document.close()
