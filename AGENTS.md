# AGENTS.md

This file provides guidance to Codex (Codex.ai/code) when working with code in this repository.

## Project Overview

SnapPDF is a PySide6 desktop GUI application that exports PDF pages to images in specified formats (PNG, JPG, WEBP, BMP, etc.).

## Tech Stack

- **Python**: 3.14+
- **GUI Framework**: PySide6 6.11.0
- **PDF Engine**: PySide6.QtPdf
- **Package Manager / Build System**: uv (uv_build backend)
- **UI Files**: Qt Designer `.ui` files, converted to Python via `pyside6-uic.exe`

## Common Commands

```bash
# Run the application
uv run snappdf

# Install dependencies
uv sync

# Convert .ui file to Python
.venv/Scripts/pyside6-uic.exe -o src/snappdf/ui_main_window.py src/snappdf/main_window.ui
```

## Project Structure

```
src/snappdf/
  __init__.py          # 入口: main() 函数, QApplication 创建
  main_window.ui       # Qt Designer XML UI 文件（布局唯一真相源）
  ui_main_window.py    # 由 .ui 文件生成，禁止手动编辑
  theme.py             # 色彩配置与 QSS 样式表
  main_window.py       # MainWindow 主窗口逻辑
  converter.py         # PDF 转图片的工作线程
```

## Architecture Notes

- **Entry point**: `snappdf:main` (declared in `pyproject.toml` `[project.scripts]`)
- **UI workflow**: Design layouts in Qt Designer (`.ui` files), convert to Python with `pyside6-uic.exe`, never hand-edit the generated Python files
- **Source layout**: Uses `src/` layout — all package code lives under `src/snappdf/`
- **Signal/Slot**: `setupUi()` 内部已调用 `QMetaObject.connectSlotsByName`，槽函数用 `@Slot` 装饰器，命名格式 `on_<objectName>_<signalName>`
- **Threading**: PDF conversion runs in `QThread` (via `ConvertWorker`) to avoid blocking the UI
- **Theme**: Dark theme colors defined in `theme.py`, applied via QSS stylesheet
- **Code style**: 中文文档注释、类型注解、PySide6 6.11.0 最新枚举写法（如 `Qt.AlignmentFlag.AlignCenter`）
