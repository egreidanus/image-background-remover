# Image Background Remover

A lightweight Linux desktop utility for removing image backgrounds using `rembg` with a simple GUI file picker powered by `zenity`.

Version: **1.0.0**  
Author: **Eelco Greidanus**  
Target OS: **Arch Linux**

## Platform Support

This project is **built and tested exclusively for Arch Linux**.

There is **no official support or guarantees** for any other Linux distributions or operating systems.

## Features

- Simple GUI file selection using Zenity
- Fast background removal using `rembg`
- Clean CLI-style progress spinner
- Automatic output naming
- Minimal dependencies
- Arch Linux optimized setup

## Dependencies

You must install the following packages:

### 1. System packages (Arch Linux)

```bash
sudo pacman -S python python-pip zenity
````

### 2. Python packages

```bash
pip install rembg
```

If you encounter missing backend dependencies for `rembg`, install:

```bash
pip install onnxruntime
```

## 🧠 Install rembg model (optional but recommended)

The app uses:

```
birefnet-massive
```

Make sure `rembg` can access models automatically. If not:

```bash
rembg install birefnet-massive
```

## Usage

Run the script:

```bash
python main.py
```

### Workflow:

1. Select input image
2. Choose output location
3. Wait for processing
4. Done ✔ background removed image saved

## Requirements

* Arch Linux (required)
* Python 3.10+
* Zenity (GTK file dialogs)
* Internet (for first model download if needed)


## Notes

* This tool is designed for desktop environments only.
* Requires a graphical session (Zenity will not work in pure TTY).
* Performance depends on CPU/GPU availability via `onnxruntime`.


## Example

```bash
python main.py
```

Output:

```
[Image Background Remover] Choose a file to process
[Image Background Remover] Input: image.png
[Image Background Remover] Output: image_nobg.png
Done ✔
```


## Disclaimer

This project is provided as-is with no guarantees.
No support is provided for non-Arch Linux systems or modified environments.

```
