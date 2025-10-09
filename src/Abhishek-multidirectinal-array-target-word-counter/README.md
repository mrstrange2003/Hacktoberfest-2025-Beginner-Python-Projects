# Multidirectional Word Search (XMAS finder)

This small Python script searches a text grid for occurrences of the word `XMAS` in all eight directions (horizontal, vertical, and both diagonals).

File: `multidirectinal-word.py`

## Description

The script reads a plain text file named `input-file` (in the same directory) that contains a rectangular grid of characters. It scans the grid and counts how many times the word `XMAS` appears. The search covers all 8 directions from each cell: left, right, up, down, and the four diagonals.

## Input format

- The script expects a file called `input-file` placed next to the script.
- Each line in `input-file` represents a row in the grid.
- Lines should all have the same length (rectangular grid). Characters are matched exactly (case-sensitive).

Example `input-file`:

```
XMAST
ABXMA
XMASC
XXXXS
```

## Usage

Run the script with Python 3:

```bash
python3 multidirectinal-word.py
```

The script will print the total number of occurrences of `XMAS` found in the grid.

## Changing the target word

The target word is currently hard-coded as `XMAS` in `multidirectinal-word.py`. To search for a different word, open the script and change the `target` variable inside the `count_xmas` function to the word you want (keep it uppercase if your grid uses uppercase letters, or adjust for case sensitivity).

## Notes and edge cases

- The search is case-sensitive. If you want case-insensitive matching, normalize the grid and the `target` (e.g., convert all characters to upper or lower case) before searching.
- If your `input-file` contains trailing spaces or empty lines, consider cleaning it or updating the script to ignore them.
- The script assumes a rectangular grid — lines of different lengths may cause index errors.

## License

This repository contains community contributions. Use and modify the script freely; add a LICENSE file to specify a license if you plan to redistribute.
