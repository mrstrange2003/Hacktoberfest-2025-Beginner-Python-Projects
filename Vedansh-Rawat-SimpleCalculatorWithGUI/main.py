import customtkinter as ctk

# Appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# App window
app = ctk.CTk()
app.title("Basic Calc")
app.geometry("400x620")
app.configure(fg_color="#030301")  # Base background
app.resizable(False, False)

# Display
display = ctk.CTkEntry(app, width=360, height=70, font=("Arial", 28),
                       justify="right", text_color="#FFFFF3", fg_color="#1a1a1a")
display.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

# Button layout
buttons = [
    ("C", 1, 0), ("X", 1, 1), ("(", 1, 2), (")", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("+", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("*", 4, 3),
    (".", 5, 0), ("0", 5, 1), ("%", 5, 2), ("/", 5, 3),
    ("=", 6, 0)  # spans all 4 columns
]

# Button click logic
def on_click(value):
    if value == "=":
        try:
            result = eval(display.get())
            display.delete(0, ctk.END)
            display.insert(0, str(result))
        except:
            display.delete(0, ctk.END)
            display.insert(0, "Error")
    elif value == "C":
        display.delete(0, ctk.END)
    elif value == "X":
        current = display.get()
        display.delete(0, ctk.END)
        display.insert(0, current[:-1])
    else:
        display.insert(ctk.END, value)

# Create buttons

operator_keys = {"+", "-", "*", "/", "%", "(", ")", "=","X","."}
number_keys = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

for (text, row, col) in buttons:
    colspan = 4 if text == "=" else 1

    if text == "C":
        fg_color = "#DB162F"
        text_color = "#FFFFFF"
    elif text == "=":
        fg_color = "#696773"
        text_color = "black"
    elif text in number_keys:
        fg_color = "#1a1a1a"
        text_color = "#FFFFF3"
    elif text in operator_keys:
        fg_color = "#1a1a1a"
        text_color = "#388697"
    else:
        fg_color = "#B7AD99"
        text_color = "#FFFFFF"

    btn = ctk.CTkButton(app, text=text,
                        width=80 * colspan + 10 * (colspan - 1),
                        height=60, font=("Arial", 20),
                        corner_radius=30,
                        fg_color=fg_color, text_color=text_color,
                        hover_color="#333333",
                        command=lambda val=text: on_click(val))
    btn.grid(row=row, column=col, columnspan=colspan, padx=10, pady=10)

app.mainloop()