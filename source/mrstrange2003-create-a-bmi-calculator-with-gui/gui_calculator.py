import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        if height > 2.8:  # Assuming input is in cm
            height = height / 100  # Convert to meters
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 24.9:
            category = "Normal weight"
        elif bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"
        label_result.config(text=f"BMI: {bmi} ({category})")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for weight and height.")

# GUI Setup
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("350x250")
root.resizable(False, False)

# Labels
tk.Label(root, text="Weight (kg):").pack(pady=(20, 5))
entry_weight = tk.Entry(root)
entry_weight.pack()

tk.Label(root, text="Height (cm):").pack(pady=(10, 5))
entry_height = tk.Entry(root)
entry_height.pack()

# Calculate Button
btn_calculate = tk.Button(root, text="Calculate BMI", command=calculate_bmi, bg="#4CAF50", fg="white")
btn_calculate.pack(pady=20)

# Result Label
label_result = tk.Label(root, text="", font=("Arial", 14, "bold"))
label_result.pack(pady=5)

root.mainloop()
