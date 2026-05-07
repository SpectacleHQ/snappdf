# Code Signing Policy

This document describes how SnapPDF intends to use code signing for release artifacts and what users should expect from signed and unsigned builds.

## Project Identity

- Project: SnapPDF
- Repository: https://github.com/SpectacleHQ/snappdf
- License: MIT License
- Primary platform: Windows desktop
- Application purpose: Convert local PDF pages to image files

SnapPDF is an open source desktop application. It processes PDF files locally on the user's machine and does not require an account, online service, or file upload to perform conversions.

## Code Signing Provider

Free code signing provided by SignPath.io, certificate by SignPath Foundation.

If accepted by SignPath Foundation, official Windows release artifacts will be signed through the SignPath.io signing workflow. The certificate publisher may appear as SignPath Foundation rather than as an individual developer or SpectacleHQ.

## Current Signing Status

Windows release artifacts are currently unsigned. Because of this, Windows Defender, Microsoft SmartScreen, or third-party antivirus products may show an unknown publisher warning or flag early downloads with low reputation.

The project plans to use open source code signing for future Windows releases. If accepted by an open source signing program such as SignPath Foundation, the Windows executable may be signed under that program's signing identity rather than under a personal developer certificate.

## Project Roles

- Authors / Committers: yuniyouguan
- Reviewers: yuniyouguan
- Signing Approvers: yuniyouguan

Only maintainers with repository write access may approve official release signing requests.

## Signing Scope

The signing policy applies to official Windows release artifacts published from this repository's GitHub Releases.

The project intends to sign:

- Windows executable files produced by the release workflow
- Windows release archives that contain the official executable, where supported by the signing workflow

The project does not intend to sign:

- Locally modified builds
- Artifacts built from forks
- Debug builds
- Files that are not produced by the official release workflow
- Third-party tools downloaded separately by users

## Build Provenance

Official releases are built from the public source code in this repository. The release workflow is stored at:

```text
.github/workflows/release.yml
```

The workflow runs when a version tag matching `v*` is pushed. It checks out the repository, installs Python and project dependencies, builds platform artifacts with PySide6 deploy tooling, and uploads release archives to GitHub Releases.

This public build process is intended to make it possible for users, reviewers, and signing providers to trace a release artifact back to the source repository and tagged revision.

## What a Signature Means

A valid signature on an official SnapPDF Windows release means:

- The signed file was approved for signing by the project's release process.
- The file has not been modified since it was signed.
- Windows can display publisher information instead of treating the file as an entirely unknown binary.

A signature does not mean:

- The software is free from all bugs.
- The signing provider independently audited all source code.
- A third-party mirror or repackaged copy is official.

Users should download official releases from:

```text
https://github.com/SpectacleHQ/snappdf/releases
```

## Privacy and Network Behavior

SnapPDF is designed to convert files locally. The application logic does not upload PDF files, exported images, or document contents to a remote server.

This program will not transfer any information to other networked systems unless specifically requested by the user or the person installing or operating it.

If future features require network access, the README and this policy should be updated before those features are released.

## Dependency Sources

SnapPDF is built with Python, PySide6, QtPdf, uv, and PySide6 deployment tooling. Release builds should use dependencies resolved from the project's lockfile and package metadata.

Bundled runtime files may include Python, Qt, PySide6, and compiler/runtime components required for the desktop application to run. These third-party components remain under their own upstream licenses and are included only as application runtime dependencies.

## Security Reports

For non-sensitive issues, please use GitHub Issues:

```text
https://github.com/SpectacleHQ/snappdf/issues
```

For security-sensitive reports, contact the maintainer by email:

```text
niyouguanyu@gmail.com
```

Please include a clear description, affected version, reproduction steps, and any relevant files or logs that can be safely shared.

## Maintainer Commitments

The project maintainer should:

- Keep the release workflow public and reviewable.
- Avoid signing binaries that cannot be traced to this repository's release process.
- Avoid signing unrelated software under the SnapPDF project.
- Update this policy if the signing provider, release process, privacy behavior, or artifact scope changes.
