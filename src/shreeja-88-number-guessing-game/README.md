# Number Guessing Game using Binary Search in Python

This Python program implements a **number guessing game** using the **binary search algorithm**.  
The computer tries to guess the number you are thinking of within a given range — efficiently narrowing down possibilities after each response.

---

## How It Works
1. You provide a **start** and **end** range.  
2. Think of any number in that range (but don’t tell the program ).  
3. The computer will **guess the middle number** and ask if it’s correct.  
4. Based on your “Yes” or “No” responses, it adjusts the range and continues guessing until it finds the number.

---

## Algorithm Explanation
This program uses the **Binary Search** approach:
- Find the midpoint of the current range.  
- If the guess is correct → stop.  
- If the number is higher → search the right half.  
- If the number is lower → search the left half.  
- Continue recursively until the correct number is found or the range becomes invalid.

---
## Features

- Interactive and fun guessing experience
- Efficient binary search logic
- Input validation for incorrect responses

## Time & Space Complexity

- Time Complexity: O(log N) — where N is the size of the range
- Space Complexity: O(log N) — due to recursive calls

---

## Example Run
    ```python
    Number Guessing Game in Python
    Enter Start Range: 1
    Enter End Range: 100
    Think of a number between 1 and 100. I will try to guess it!
    Is the number 50? (Y/N): n
    Is the actual number greater than 50? (Y/N): y
    Is the number 75? (Y/N): y
    Congratulation To me! Successfully Guessed Number

