# libjpeg-turbo-build

`libjpeg-turbo` を以下のターゲット向けに生成します。

- Windows: `x86`, `x64`
- Linux: `x86_64`, `aarch64`
- Android: `x86_64`, `arm64-v8a`

## ビルド

`libjpeg-turbo` のソース一式を以下からダウンロードします。

- <https://github.com/libjpeg-turbo/libjpeg-turbo/releases/tag/2.1.1>

### Windows

インテルx86系のアセンブラ `nasm` をインストールしておく必要がある。

```bash
$ python build_window.py
```

### Linux

```bash
$ python build_linux.py
```

### Android

```bash
$ python build_android.py
```
