"""
SnapPDF - PDF 页面导出为图片工具。

基于 PySide6 构建的桌面应用，支持将 PDF 每一页导出为
PNG、JPG、WEBP、BMP 等格式的图片。
"""

import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

# 导入资源文件以注册图标
from snappdf.assets import resources_rc  # noqa: F401
from snappdf.main_window import MainWindow
from snappdf.theme import build_stylesheet


def main() -> None:
    """SnapPDF 应用入口。"""
    app = QApplication(sys.argv)
    app.setApplicationName("SnapPDF")
    app.setApplicationVersion("1.0.0")
    app.setWindowIcon(QIcon(":/icons/app_icon.ico"))
    app.setStyleSheet(build_stylesheet())

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
