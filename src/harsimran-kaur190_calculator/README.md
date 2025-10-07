# Calculator in Python 🧮

A command-line Python calculator that supports multiple arithmetic and mathematical operations with input validation, calculation history, and the ability to save history to a file.

---

## Features

- **Basic arithmetic operations:**
  - Addition
  - Subtraction
  - Multiplication
  - Division (with zero-division check)
- **Advanced operations:**
  - Square root
  - Power
  - Factorial
  - Average of multiple numbers
  - Percentage calculation
- **Input validation** to prevent invalid entries
- **Calculation history** stored in memory during a session
- Option to **save session history** to a `history.txt` file
- Graceful handling of **keyboard interrupts** (Ctrl + C)
- **User-friendly CLI interface**

---

## How to Use

1. Run the program:

```bash
python calculator.py
```

2. You will see a menu of operations

3. Enter the name of the operation (e.g., add, subtract).
Inputs are case-insensitive and ignore spaces.

4. Follow prompts to enter numbers:
- Division checks for zero
- Factorial and square root require non-negative numbers

5. After each calculation, you can choose to continue or exit.

6. When exiting, you can optionally view or save your calculation history.

## Example Usage
```Please enter the required operation name: add
Enter first number: 5
Enter second number: 10
5 + 10 = 15.0
Do you want to continue(YES/NO)? yes

Do you want to see history(YES/NO)? yes
1. 5 + 10 = 15.0
```

## Saving History
If you choose to save, the session will be stored in history.txt with a timestamp:
```
Session at 07/10/2025, 08:00:00
5 + 10 = 15.0
```

## Requirements
- Python 3.x
- Standard libraries only (math, datetime)