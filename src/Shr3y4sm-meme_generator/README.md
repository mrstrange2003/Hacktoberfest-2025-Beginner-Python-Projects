# Simple Meme Generator

A simple Python-based meme generator with a graphical user interface that allows users to:

- Select an image
- Add top text
- Add bottom text
- Generate and save memes

## Examples

Here are some examples of memes created using this generator:

### Input Image

![Input Image](examples/input.jpg)

### Generated Meme

![Generated Meme](examples/output.png)

The meme generator adds white text with black outline for better visibility on any background. Text is automatically sized and centered based on the image dimensions.

## Requirements

- Python 3.x
- Pillow (PIL)
- tkinter (usually comes with Python)

## Installation

```bash
pip install Pillow
```

## How to Use

1. Run the program:

   ```bash
   python meme_generator.py
   ```

2. Click "Select Image" to choose your base image
3. Enter your desired top and bottom text
4. Click "Generate Meme"
5. Choose where to save your meme

## Features

- Simple and intuitive GUI
- Support for various image formats (JPG, PNG, BMP, GIF, TIFF)
- Automatically sized text based on image dimensions
- White text with black outline for visibility
- Text is automatically centered
- Error handling for better user experience

## Notes

- Text will be automatically converted to uppercase for the classic meme look
- The font will default to system font if Arial is not available
- Images are saved in PNG format
