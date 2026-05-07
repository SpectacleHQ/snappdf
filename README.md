# SnapPDF

SnapPDF 是一个开源桌面工具，用于将 PDF 页面批量导出为 PNG、JPG、WEBP 或 BMP 图片。

它基于 Python、PySide6 和 QtPdf 构建，转换过程在本机完成，不需要上传 PDF 文件，也不依赖在线服务。

## 功能

- 将 PDF 页面导出为 PNG、JPG、WEBP、BMP 图片
- 支持自定义 DPI：72、150、200、300、600
- 支持 JPG / WEBP 图片质量设置
- 支持页面范围导出，例如 `1-3, 5, 7-9`
- 支持拖拽 PDF 文件到窗口中
- 支持选择自定义输出目录
- 使用后台线程执行转换，避免界面卡住

## 下载

最新版本请在 GitHub Releases 下载：

- 仓库地址：https://github.com/SpectacleHQ/snappdf
- v1.0.0 发布页：https://github.com/SpectacleHQ/snappdf/releases/tag/v1.0.0

目前发布包尚未进行 Windows 代码签名。首次运行时，Windows Defender、SmartScreen 或其他安全软件可能会显示未知发布者提示。这通常是因为该版本还没有代码签名证书和下载信誉，并不表示 SnapPDF 会联网收集或上传你的文件。

Code signing policy: [docs/code-signing-policy.md](docs/code-signing-policy.md)

如果你不想直接运行未签名二进制文件，可以从源码运行：

```bash
uv sync
uv run snappdf
```

## 使用方法

1. 打开 SnapPDF。
2. 将 PDF 文件拖入窗口，或点击拖拽区域选择 PDF。
3. 选择导出格式、DPI、图片质量和页面范围。
4. 选择输出目录。
5. 点击转换，等待导出完成。

页面范围可以留空，表示导出全部页面。也可以输入：

```text
1-3, 5, 7-9
```

## 从源码开发

项目使用 `uv` 管理依赖和运行环境。

```bash
# 安装依赖
uv sync

# 运行应用
uv run snappdf
```

如果修改了 Qt Designer 的 `.ui` 文件，需要重新生成 Python UI 文件：

```bash
.venv/Scripts/pyside6-uic.exe -o src/snappdf/ui_main_window.py src/snappdf/main_window.ui
```

注意：`src/snappdf/main_window.ui` 是界面布局的来源，`src/snappdf/ui_main_window.py` 是生成文件，请不要手动编辑。

## 构建与发布

SnapPDF 使用 GitHub Actions 在打 tag 时构建发布包：

- Windows x64：打包为 `SnapPDF-<version>-windows-x64.zip`
- macOS arm64：打包为 `SnapPDF-<version>-macos-arm64.zip`

发布 workflow 位于 `.github/workflows/release.yml`。发布产物由公开仓库中的源码、构建脚本和 GitHub Actions 环境生成，方便用户和审核方追溯来源。

## 安全与隐私

- SnapPDF 在本机读取 PDF 并导出图片。
- 当前应用逻辑不需要账户、云服务或网络上传。
- 如果下载的是未签名版本，Windows 可能会给出安全提示；这是代码签名和应用信誉问题，不等同于恶意软件判定。
- 项目计划申请开源代码签名，以降低 Windows 用户安装和运行时的误报与拦截。

Code signing policy: [docs/code-signing-policy.md](docs/code-signing-policy.md)

## 技术栈

- Python 3.14+
- PySide6 6.11+
- PySide6.QtPdf
- uv / uv_build

## 许可证

SnapPDF 使用 MIT License 开源。详情见 [LICENSE](LICENSE)。
