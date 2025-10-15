 # Basic Calc – A CustomTkinter GUI Calculator
Basic Calc is a sleek, dark-themed calculator built using CustomTkinter, a modern UI framework for Python. It supports basic arithmetic operations and features a clean, responsive layout with custom-styled buttons.

 ## Features
- Dark mode interface with blue accent theme
- Responsive button grid with hover effects
- Supports:
- Addition, subtraction, multiplication, division
- Parentheses and decimal input
- Percentage calculation
- Clear (C) and backspace (X) functionality
- Error handling for invalid expressions

 ## UI Overview
- Display: Large entry field aligned to the right for input and results
- Buttons:
- Digits: 0–9
- Operators: +, -, *, /, %, (, )
- Controls: C (clear), X (backspace), = (evaluate)

 ## How It Works
- Button clicks trigger the on_click() function.
- Input is dynamically inserted into the display field.
- On =, the expression is evaluated using Python’s eval() function.
- Errors (e.g., malformed expressions) are caught and shown as "Error".

 ## Installation
- Install CustomTkinter:
`` pip install customtkinter ``
- Clone or copy the script and run it with Python 3:
`` python main.py ``