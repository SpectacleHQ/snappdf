"""
SnapPDF 主题色彩与样式定义。

基于 ui-ux-pro-max 设计系统生成的深色主题配色方案。
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ColorPalette:
    """SnapPDF 色彩配置。"""

    # 主色调
    primary: str = "#EA580C"
    on_primary: str = "#FFFFFF"

    # 辅助色
    secondary: str = "#2563EB"
    on_secondary: str = "#FFFFFF"

    # 背景与表面
    background: str = "#0F172A"
    surface: str = "#1B2336"
    surface_hover: str = "#272F42"

    # 文本
    foreground: str = "#F8FAFC"
    muted: str = "#94A3B8"

    # 边框
    border: str = "#334155"

    # 语义色
    success: str = "#22C55E"
    error: str = "#DC2626"
    warning: str = "#F59E0B"


COLORS = ColorPalette()


def build_stylesheet() -> str:
    """生成 SnapPDF 全局 QSS 样式表。"""

    c = COLORS
    return f"""
    /* === 全局 === */
    QMainWindow, QWidget#centralwidget {{
        background-color: {c.background};
        color: {c.foreground};
    }}

    /* === 标题区 === */
    QLabel {{
        background: transparent;
    }}

    /* === 拖拽区域 === */
    QFrame#dropZoneFrame {{
        background-color: {c.surface};
        border: 2px dashed {c.border};
        border-radius: 12px;
    }}
    QFrame#dropZoneFrame:hover {{
        border-color: {c.primary};
    }}

    /* === 设置面板 === */
    QFrame#settingsFrame {{
        background-color: {c.surface};
        border: 1px solid {c.border};
        border-radius: 12px;
        padding: 16px;
    }}

    /* === 进度面板 === */
    QFrame#progressFrame {{
        background-color: {c.surface};
        border: 1px solid {c.border};
        border-radius: 12px;
        padding: 12px;
    }}

    /* === 下拉框 === */
    QComboBox {{
        background-color: {c.surface_hover};
        color: {c.foreground};
        border: 1px solid {c.border};
        border-radius: 8px;
        padding: 6px 12px;
        font-size: 13px;
    }}
    QComboBox:hover {{
        border-color: {c.muted};
    }}
    QComboBox:focus {{
        border-color: {c.primary};
    }}
    QComboBox::drop-down {{
        border: none;
        width: 24px;
    }}
    QComboBox QAbstractItemView {{
        background-color: {c.surface};
        color: {c.foreground};
        border: 1px solid {c.border};
        selection-background-color: {c.surface_hover};
    }}

    /* === 输入框 === */
    QLineEdit {{
        background-color: {c.surface_hover};
        color: {c.foreground};
        border: 1px solid {c.border};
        border-radius: 8px;
        padding: 6px 12px;
        font-size: 13px;
    }}
    QLineEdit:hover {{
        border-color: {c.muted};
    }}
    QLineEdit:focus {{
        border-color: {c.primary};
    }}

    /* === 滑块 === */
    QSlider::groove:horizontal {{
        background: {c.surface_hover};
        height: 6px;
        border-radius: 3px;
    }}
    QSlider::handle:horizontal {{
        background: {c.primary};
        width: 18px;
        height: 18px;
        margin: -6px 0;
        border-radius: 9px;
    }}
    QSlider::sub-page:horizontal {{
        background: {c.primary};
        border-radius: 3px;
    }}

    /* === 进度条 === */
    QProgressBar {{
        background-color: {c.surface_hover};
        border: none;
        border-radius: 4px;
    }}
    QProgressBar::chunk {{
        background-color: {c.primary};
        border-radius: 4px;
    }}

    /* === 主按钮（转换） === */
    QPushButton#convertBtn {{
        background-color: {c.primary};
        color: {c.on_primary};
        border: none;
        border-radius: 12px;
        font-size: 16px;
        font-weight: 700;
    }}
    QPushButton#convertBtn:hover {{
        background-color: #F97316;
    }}
    QPushButton#convertBtn:pressed {{
        background-color: #C2410C;
    }}
    QPushButton#convertBtn:disabled {{
        background-color: {c.surface_hover};
        color: {c.muted};
    }}

    /* === 浏览按钮 === */
    QPushButton#browseOutputBtn {{
        background-color: {c.surface_hover};
        color: {c.foreground};
        border: 1px solid {c.border};
        border-radius: 8px;
        font-size: 13px;
    }}
    QPushButton#browseOutputBtn:hover {{
        border-color: {c.muted};
        background-color: #334155;
    }}
    QPushButton#browseOutputBtn:pressed {{
        background-color: {c.border};
    }}
    """
