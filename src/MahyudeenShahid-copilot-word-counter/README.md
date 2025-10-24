# Word Counter

A simple Python application that counts the number of words, characters, and lines in text. The program can analyze both direct text input and text files.

## Features

- Count words in text
- Count characters (including whitespace)
- Count lines
- Support for both direct text input and text file analysis
- UTF-8 encoding support

## Requirements

- Python 3.x

No additional packages are required as this project uses only Python's standard library.

## Usage

1. Run the program:
   ```bash
   python main.py
   ```

2. Choose your input method:
   - Option 1: Enter text directly
   - Option 2: Analyze a text file

### Direct Text Input

1. Choose option 1
2. Type or paste your text
3. Press Ctrl+D (Unix) or Ctrl+Z (Windows) when done
4. View the analysis results

### Text File Analysis

1. Choose option 2
2. Enter the path to your text file
3. View the analysis results

## Example Output

```
Welcome to Word Counter!
1. Enter text directly
2. Analyze a text file

Enter your choice (1 or 2): 1

Enter your text (press Ctrl+D or Ctrl+Z on Windows when done):
Hello world!
This is a test.
^Z

Analysis Results:
Words: 5
Characters: 26
Lines: 2
```

## Error Handling

The program includes error handling for:
- File not found errors
- File reading errors
- Invalid input choices

---
Developed by Mahyudeen Shahid with ❤