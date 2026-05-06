# SnapPDF

将 PDF 每一页导出为指定格式图片的桌面工具。

## 功能

- 支持输出 PNG、JPG、WEBP、BMP 格式
- 自定义 DPI（72 / 150 / 200 / 300 / 600）
- 自定义图片质量（JPG / WEBP）
- 指定页面范围导出（如 `1-3, 5, 7-9`）
- 拖拽或点击选择 PDF 文件
- 自定义输出目录
- 后台线程转换，不阻塞界面

## 快速开始

```bash
# 安装依赖
uv sync

# 运行
uv run snappdf
```

## 依赖

- Python 3.14+
- PySide6 6.11+
- PySide6.QtPdf
