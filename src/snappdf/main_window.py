"""
SnapPDF 主窗口模块。

负责界面交互逻辑、文件选择、参数配置和调用转换线程。
"""

import re
from pathlib import Path

from PySide6.QtCore import Slot
from PySide6.QtGui import QDragEnterEvent, QDropEvent
from PySide6.QtWidgets import QFileDialog, QMainWindow

from snappdf.converter import ConvertWorker, get_pdf_page_count
from snappdf.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    """SnapPDF 主窗口。"""

    def __init__(self) -> None:
        """初始化主窗口，绑定信号与槽函数。"""
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._pdf_path: str = ""
        self._worker: ConvertWorker | None = None

        self.setAcceptDrops(True)
        self.ui.dropZoneFrame.setAcceptDrops(True)

        # 初始化质量控件可见性（默认 PNG，无质量参数）
        self.on_formatComboBox_currentTextChanged(
            self.ui.formatComboBox.currentText()
        )

    # ── 拖拽事件 ──────────────────────────────────────────

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        """拖入事件：接受 PDF 文件。"""
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                if url.toLocalFile().lower().endswith(".pdf"):
                    event.acceptProposedAction()
                    return
        event.ignore()

    def dropEvent(self, event: QDropEvent) -> None:
        """放下事件：加载 PDF 文件。"""
        for url in event.mimeData().urls():
            path = url.toLocalFile()
            if path.lower().endswith(".pdf"):
                self._load_pdf(path)
                break

    def mousePressEvent(self, event) -> None:
        """鼠标点击事件：点击拖拽区域时打开文件选择。"""
        super().mousePressEvent(event)
        if self.ui.dropZoneFrame.underMouse():
            path, _ = QFileDialog.getOpenFileName(
                self, "选择 PDF 文件", "", "PDF 文件 (*.pdf)"
            )
            if path:
                self._load_pdf(path)

    # ── 自动连接的槽函数 ──────────────────────────────────

    @Slot(str)
    def on_formatComboBox_currentTextChanged(self, text: str) -> None:
        """
        格式切换时更新质量控件的可见状态。

        PNG 和 BMP 是无损格式，不支持质量参数。

        Args:
            text: 当前选中的格式名称。
        """
        lossless = text.upper() in ("PNG", "BMP")
        self.ui.qualityLabel.setVisible(not lossless)
        self.ui.qualitySlider.setVisible(not lossless)
        self.ui.qualityValueLabel.setVisible(not lossless)

    @Slot(int)
    def on_qualitySlider_valueChanged(self, value: int) -> None:
        """
        质量滑块值变化时更新显示。

        Args:
            value: 当前滑块值（1-100）。
        """
        self.ui.qualityValueLabel.setText(f"{value}%")

    @Slot()
    def on_browseOutputBtn_clicked(self) -> None:
        """打开输出目录选择对话框。"""
        path = QFileDialog.getExistingDirectory(self, "选择输出目录")
        if path:
            self.ui.outputDirEdit.setText(path)

    @Slot()
    def on_convertBtn_clicked(self) -> None:
        """开始转换。"""
        if not self._pdf_path:
            return

        output_dir = self.ui.outputDirEdit.text()
        if not output_dir:
            output_dir = str(Path(self._pdf_path).parent)

        fmt = self.ui.formatComboBox.currentText().lower()
        quality = self.ui.qualitySlider.value()
        dpi = int(self.ui.dpiComboBox.currentText())
        pages = self._parse_page_range(
            self.ui.pageRangeEdit.text(), self._get_page_count()
        )

        self._set_ui_enabled(False)
        self.ui.progressLabel.setText("正在转换...")

        self._worker = ConvertWorker(
            pdf_path=self._pdf_path,
            output_dir=output_dir,
            fmt=fmt,
            quality=quality,
            dpi=dpi,
            pages=pages,
        )
        self._worker.progress_changed.connect(self._on_progress)
        self._worker.finished_all.connect(self._on_finished)
        self._worker.error_occurred.connect(self._on_error)
        self._worker.start()

    # ── 内部方法 ──────────────────────────────────────────

    def _load_pdf(self, path: str) -> None:
        """
        加载 PDF 文件并更新界面。

        Args:
            path: PDF 文件的绝对路径。
        """
        self._pdf_path = path
        name = Path(path).name
        self.ui.fileNameLabel.setText(name)
        self.ui.dropTextLabel.setText("已选择文件")
        self.ui.dropIconLabel.setText("✅")
        self.ui.convertBtn.setEnabled(True)

    def _get_page_count(self) -> int:
        """获取 PDF 总页数。"""
        try:
            return get_pdf_page_count(self._pdf_path)
        except Exception:
            return 0

    @staticmethod
    def _parse_page_range(text: str, total: int) -> list[int] | None:
        """
        解析页码范围字符串。

        Args:
            text: 页码范围字符串，如 "1-3, 5, 7-9"。
            total: PDF 总页数。

        Returns:
            页码列表（0-indexed），None 表示全部页面。
        """
        text = text.strip()
        if not text:
            return None

        pages: list[int] = []
        for part in re.split(r"[,，\s]+", text):
            part = part.strip()
            if not part:
                continue
            if "-" in part:
                start_str, end_str = part.split("-", 1)
                start = int(start_str) - 1
                end = int(end_str) - 1
                pages.extend(range(start, min(end + 1, total)))
            else:
                page = int(part) - 1
                if 0 <= page < total:
                    pages.append(page)

        return sorted(set(pages)) if pages else None

    def _on_progress(self, current: int, total: int, name: str) -> None:
        """
        更新转换进度。

        Args:
            current: 当前已完成页数。
            total: 总页数。
            name: 当前输出文件名。
        """
        percent = int(current / total * 100)
        self.ui.progressBar.setValue(percent)
        self.ui.progressPercentLabel.setText(f"{percent}%")
        self.ui.progressLabel.setText(f"正在处理: {name}")

    def _on_finished(self, paths: list[str]) -> None:
        """
        转换完成回调。

        Args:
            paths: 所有输出文件路径列表。
        """
        self._set_ui_enabled(True)
        self.ui.progressLabel.setText(f"转换完成，共 {len(paths)} 个文件")
        self.ui.progressPercentLabel.setText("100%")
        self.ui.progressBar.setValue(100)

    def _on_error(self, message: str) -> None:
        """
        转换出错回调。

        Args:
            message: 错误信息。
        """
        self._set_ui_enabled(True)
        self.ui.progressLabel.setText(message)
        self.ui.progressBar.setValue(0)
        self.ui.progressPercentLabel.setText("")

    def _set_ui_enabled(self, enabled: bool) -> None:
        """
        设置界面控件的启用状态。

        Args:
            enabled: 是否启用。
        """
        self.ui.convertBtn.setEnabled(enabled and bool(self._pdf_path))
        self.ui.browseOutputBtn.setEnabled(enabled)
        self.ui.formatComboBox.setEnabled(enabled)
        self.ui.dpiComboBox.setEnabled(enabled)
        self.ui.pageRangeEdit.setEnabled(enabled)
        # 质量控件可见性由格式决定，这里只处理启用状态
        fmt = self.ui.formatComboBox.currentText().upper()
        if fmt not in ("PNG", "BMP"):
            self.ui.qualitySlider.setEnabled(enabled)
            self.ui.qualityValueLabel.setEnabled(enabled)
            self.ui.qualityLabel.setEnabled(enabled)
