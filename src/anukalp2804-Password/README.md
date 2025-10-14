🔐 Password Strength Checker

A simple and efficient Python project that checks the strength of a password based on several security parameters such as length, uppercase/lowercase letters, numbers, and special characters.

🚀 Features

Checks password length (minimum recommended 8 characters)

Verifies presence of:

1. Uppercase letters
2. Lowercase letters
3. Digits (0–9)
4. Special characters (@, #, $, %, etc.)
5. Rates passwords as:

a. Weak
b. Moderate
c. Strong

Provides feedback on how to improve weak passwords
No external libraries required (uses only built-in Python modules)

🧠 How It Works

The program uses simple string checks and conditions to analyze a given password.
It evaluates the strength based on:
Password length
1. Character variety (uppercase, lowercase, digits, symbols)
A score is generated internally, and based on that score, the program categorizes the password.

💻 How to Run

1. Save the file as password_strength_checker.py
2. Open your terminal or command prompt
3. Run the program:
4. python password_strength_checker.py
5. Enter a password when prompted:
6. Enter your password: Hello@123
7. Password Strength: Strong ✅

🧩 Example Outputs
Enter your password: abc
Password Strength: Weak ❌
Suggestion: Add uppercase letters, digits, and special symbols.

Enter your password: Hello123
Password Strength: Moderate ⚠️
Suggestion: Add special characters to make it stronger.

Enter your password: Hello@123
Password Strength: Strong ✅

🧾 Requirements

Python 3.x

Uses built-in libraries only (no installation required)

🌟 Future Enhancements

GUI version using Tkinter

Real-time strength bar while typing

Option to check password leaks using an API

👨‍💻 Author

Anukalp Pandey
📧 pandeyanukalp6@gmail.com
🌐 anukalp2804