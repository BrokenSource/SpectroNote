<div align="center">
  <img src="https://raw.githubusercontent.com/BrokenSource/SpectroNote/main/website/assets/logo.png" width="200">
  <h1>SpectroNote</h1>
  <span>Piano-perfect audio spectrogram</span>
  <br>
  <br>
    <a href="https://pypi.org/project/spectronote/"><img src="https://img.shields.io/pypi/v/spectronote?label=PyPI&color=blue"></a>
    <a href="https://pypi.org/project/spectronote/"><img src="https://img.shields.io/pypi/dw/spectronote?label=%E2%86%93&color=blue"></a>
    <a href="https://github.com/BrokenSource/SpectroNote/"><img src="https://img.shields.io/github/v/tag/BrokenSource/SpectroNote?label=GitHub&color=orange"></a>
    <a href="https://github.com/BrokenSource/SpectroNote/stargazers/"><img src="https://img.shields.io/github/stars/BrokenSource/SpectroNote?label=Stars&style=flat&color=orange"></a>
    <a href="https://github.com/BrokenSource/SpectroNote/releases/"><img src="https://img.shields.io/github/v/release/BrokenSource/SpectroNote?label=Release&color=light-green"></a>
    <a href="https://github.com/BrokenSource/SpectroNote/releases/"><img src="https://img.shields.io/github/downloads/BrokenSource/SpectroNote/total?label=Downloads&color=light-green"></a>
    <a href="https://discord.gg/KjqvcYwRHm"><img src="https://img.shields.io/discord/1184696441298485370?label=Discord&style=flat&color=purple"></a>
  <br>
  <sub><small>⭐️ Consider starring the project to help it grow! ⭐️</small></sub>
  <br>
</div>

![image](https://github.com/BrokenSource/SpectroNote/assets/29046864/23d2ab9f-0c02-45bd-89f0-d8e57b7d112b)

## 🔥 Description

SpectroNote is a fast audio spectrogram written in python.

- [x] **Export Videos**: powered by the [**ShaderFlow**](https://github.com/BrokenSource/ShaderFlow) platform
- [x] **Side Piano**: instantly find notes being played
- [x] **Real Time**: it's python, scientifically made

## 📦 Installation

Until better documentation, install and run the [`spectronote`](https://pypi.org/project/spectronote/) PyPI package, either directly with <a href="https://docs.astral.sh/uv/">astral-sh/uv</a>:

```bash
uvx --python 3.13 spectronote --help
```

Or add to your `pyproject.toml` dependencies for library usage.

<b>Note:</b> Audio source defaults to the first loopback device, it may pick a wrong one or a microphone. Input selection will be handled in a future release, change it via `pavucontrol` on Linux or Settings on Windows/Mac for now.
