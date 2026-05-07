[app]

# Title of your application
title = SnapPDF

# Project root directory. Keep this relative so GitHub Actions runners can use it.
project_dir = .

# Source file entry point path. This file calls snappdf.main().
input_file = src/snappdf/app.py

# Directory where the executable output is generated
exec_directory = dist

# Path to the project file relative to project_dir
project_file = pyproject.toml

# Application icon. The release workflow swaps this to icon.icns on macOS.
icon = src/snappdf/assets/icon.ico

[python]

# Python path. Leave empty so pyside6-deploy uses the active CI/local Python.
python_path =

# Python packages to install
packages = Nuitka[onefile]==4.0.8

# Buildozer: for deploying Android application
android_packages = buildozer==1.5.0,cython==0.29.33

[qt]

# Paths to required QML files. Comma separated
qml_files =

# Excluded QML plugin binaries
excluded_qml_plugins =

# Qt modules used. Comma separated
modules = Core,Gui,Pdf,Widgets

# Qt plugins used by the application.
plugins = accessiblebridge,egldeviceintegrations,generic,iconengines,imageformats,platforminputcontexts,platforms,platforms/darwin,platformthemes,styles,wayland-decoration-client,wayland-graphics-integration-client,wayland-shell-integration,xcbglintegrations

[android]

# Path to pyside wheel
wheel_pyside =

# Path to shiboken wheel
wheel_shiboken =

# Plugins to be copied to libs folder of the packaged application. Comma separated
plugins =

[nuitka]

# Usage description for permissions requested by the app as found in the info.plist file
macos.permissions =

# Mode of using Nuitka. macOS is forced to app bundle by pyside6-deploy.
mode = onefile

# Specify any extra Nuitka arguments.
# Version metadata is embedded in Windows binaries and helps users identify official builds.
extra_args = --quiet --noinclude-qt-translations --assume-yes-for-downloads --company-name=SpectacleHQ --product-name=SnapPDF --file-version=1.0.0.0 --product-version=1.0.0.0 "--file-description=SnapPDF PDF to image converter" "--copyright=Copyright (c) 2026 yuniyouguan" "--trademarks=SnapPDF"

[buildozer]

# Build mode
mode = debug

# Path to pyside6 and shiboken6 recipe dir
recipe_dir =

# Path to extra Qt Android .jar files to be loaded by the application
jars_dir =

# If empty, uses default NDK path downloaded by buildozer
ndk_path =

# If empty, uses default SDK path downloaded by buildozer
sdk_path =

# Other libraries to be loaded at app startup. Comma separated.
local_libs =

# Architecture of deployed platform
arch =
