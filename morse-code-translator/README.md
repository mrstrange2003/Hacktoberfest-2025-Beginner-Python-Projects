# Morse Code Translator

A beginner-friendly **Morse Code Translator** written in Python.  
This project allows users to convert **plain text to Morse code** and **Morse code back to readable text** using a simple command-line interface (CLI).  
It is designed to be **easy to understand**, **educational**, and a great starting point for beginners learning Python and text manipulation.

---

## Features
- Convert **text → Morse code** with support for letters, numbers, and common punctuation.
- Convert **Morse code → text**, handling spaces using `/` for word separation.
- Terminal-based CLI; requires no additional libraries.
- Beginner-friendly code structure with functions for encryption and decryption.
- Handles invalid characters gracefully by ignoring unsupported symbols.
- Includes clear examples and documentation for easy use and understanding.

---

## About Morse Code
Morse code is a **method of encoding text** using a series of dots (`.`) and dashes (`-`).  
- Each letter, number, or symbol has a unique representation.  
- Words are separated by `/` or spaces.  
- It was historically used in telegraphy and radio communication.  

This project uses a **Python dictionary** to map characters to Morse code and vice versa, allowing quick conversion in both directions.

---

## How It Works
- **Text to Morse:** Each character from the input text is converted to its Morse equivalent using a dictionary lookup. Spaces between words are replaced with `/`.
- **Morse to Text:** The Morse code is split by spaces. Each Morse sequence is matched to its corresponding character in the dictionary. Consecutive spaces are interpreted as word separators.

---

## Example Usage

**Text to Morse**
Input: Hello World
Output: .... . .-.. .-.. --- / .-- --- .-. .-.. -..

**Morse to Text**
Input: .... . .-.. .-.. --- / .-- --- .-. .-.. -..
Output: HELLO WORLD

---

## Potential Improvements
- Add a **GUI interface** using Tkinter for a more interactive experience.
- Include support for **real-time audio beep sounds** for Morse code output.
- Allow **reading/writing from files** for batch translations.
- Implement **error checking** for invalid Morse sequences.
- Extend dictionary to include **additional symbols** like `@`, `&`, `:`.

---

## Author
[madhavansingh](https://github.com/madhavansingh)

---

## Contribution
This project is designed for beginners and is open to improvements and new features.  
Guidelines for contribution:
1. Fork the repository.
2. Create a new branch for your feature.
3. Make changes and test thoroughly.
4. Submit a Pull Request (PR) with a clear description.
5. Mention any improvements or additional features you added.

---

## Resources
- [Morse Code Wikipedia](https://en.wikipedia.org/wiki/Morse_code)
- [Python Documentation](https://docs.python.org/3/)