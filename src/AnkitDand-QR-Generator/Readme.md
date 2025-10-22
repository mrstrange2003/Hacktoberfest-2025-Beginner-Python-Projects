
# 🧩 QR Code Generator (Python CLI)

A terminal-based Python script to generate a QR code from any **text or URL**.
The script creates a PNG image with your QR code and follows a **minimal and easy-to-use design**

---

### 🎮 Features

* **Generate QR Codes:** Convert any text or URL into a QR code.
* **Save as PNG:** Output the QR code as an image file.
* **Custom Output Name:** Optionally specify a filename for the saved QR code.
* **Simple CLI:** Easy command-line usage with minimal arguments.
* **Beginner-Friendly:** Clean, readable, and minimal Python code.

---

### ⚙️ Getting Started

#### 🧠 Prerequisites

* Python 3.x installed
* `qrcode` library (install with `pip install qrcode`)

#### 🚀 How to Run

Clone or download this repository, then navigate to the project folder:

```bash
cd src/AnkitDand-QR-Generator
pip install qrcode
```

Run the script with your desired text or URL:

```bash
python qr_generator.py -t "https://www.instagram.com"
```

Optionally, specify a custom output filename:

```bash
python qr_generator.py -t "https://www.instagram.com" -o instagram_qr.png
```

---

### 🎯 How to Use

* Use the `-t` or `--text` argument to pass the text or URL to encode.
* Use the `-o` or `--output` argument to specify a filename for the generated QR code (default is `qrcode.png`).

Example:

```bash
python qr_generator.py -t "https://example.com"
```

This will create a `qrcode.png` file in the current folder containing the QR code.

---

### 🧩 Code Overview

#### `generate_qr()` Function

Handles:

* Creating the QR code
* Setting box size and border
* Saving the PNG image

#### Key Arguments

| Argument   | Description                   |
| ---------- | ----------------------------- |
| `text`     | Text or URL to encode         |
| `filename` | Name of the output file (PNG) |

---

### 💡 Project Structure

```
src/
└── AnkitDand-QR-Generator/
    ├── qr_generator.py
    └── README.md
```

