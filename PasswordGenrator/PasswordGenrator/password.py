import tkinter as tk
from tkinter import ttk
import random
import string

root = tk.Tk()
root.title("Pass-Gen")
root.geometry("400x600+400+100")
root.configure(bg="light grey")

def Generator():
    try:
        input1 = int(character.get())
        
        if input1 <= 0:
            note.configure(text="Enter a positive integer")
        else:
            password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=input1))
            result_label.configure(text=password)
    except ValueError:
        note.configure(text="Enter a valid integer")


def toggle_manual():
    if manual_text.winfo_viewable():
        manual_text.pack_forget()
        manual_button.configure(text="Show User Manual")
    else:
        manual_text.pack(fill="both", expand=True)
        manual_button.configure(text="Hide User Manual")


note = ttk.Label(root, text="Enter number of characters:", background="light grey", font=("Arial", 12))
note.pack(pady=20)


character = tk.Entry(root, font=("Arial", 12))
character.pack(pady=10)


generate_button = tk.Button(root, text="Generate Password", command=Generator, font=("Arial", 12), bg="powder blue")
generate_button.pack(pady=20)

result_label = ttk.Label(root, text="", background="#D8BFD8", font=("Arial", 12, "bold"))
result_label.pack(pady=20)


manual_button = tk.Button(root, text="Show User Manual", command=toggle_manual, font=("Arial", 12), bg="powder blue")
manual_button.pack(pady=20)


manual_text = tk.Text(root, wrap="word", bg="#FFA07A", font=("Arial", 10), padx=10, pady=10, height=15)
manual_content = """
Application Name: Pass-Gen
Version: 1.0
Author: [Suramya Ranjan]

Overview:
Pass-Gen is a simple password generator application that creates strong and random passwords based on the number of characters specified by the user.

How to Use:
1. Launch the application. You will see a window with the title "Pass-Gen".
2. In the input field labeled "Enter number of characters:", type the number of characters you want in your password.
   - Note: The input must be a positive integer. If you enter a non-integer or a negative number, an error message will be displayed.
3. Click the "Generate Password" button.
4. The generated password will be displayed below the button.

Features:
- The application generates a password containing a mix of uppercase and lowercase letters, digits, and special characters.
- The length of the password is determined by the number of characters entered by the user.
- Error handling ensures that only valid positive integers are accepted as input.

Example:
- If you enter "10" in the input field and click "Generate Password", a random 10-character password such as "A1b2C3d4E5" will be displayed.


Limitations:
- The application does not remember previously generated passwords.
- The application does not provide options for excluding certain characters or patterns (e.g., no special characters).

Troubleshooting:
- If you see the message "Enter a positive integer", make sure you enter a valid number greater than zero.
- If the application does not respond or crashes, ensure that your Python environment includes the `tkinter` and `random` modules.

Contact:
- For any issues or suggestions, contact [XXXXXXXXXX].

License:
- This project is licensed under the XYZ License. Feel free to use and modify the code as needed.
"""
manual_text.insert(tk.END, manual_content)
manual_text.config(state=tk.DISABLED)
manual_text.pack_forget()  

root.resizable(False, False)
root.mainloop()
