import threading
import time
import tkinter as tk
from tkinter import messagebox

try:
    import pyautogui
except ImportError:
    pyautogui = None


def run_typing(text, delay=5):
    """Wait `delay` seconds then type `text` using pyautogui."""
    for i in range(delay, 0, -1):
        # simple countdown printed to console (UI will be minimal)
        print(f"Starting in {i}...")
        time.sleep(1)
    # small pause to let user ensure focus
    time.sleep(0.1)
    pyautogui.typewrite(text, interval=0.02)


class SimpleTyper(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Beginner Typer')
        self.geometry('420x120')
        self.resizable(False, False)

        self.entry = tk.Entry(self, font=('Segoe UI', 11))
        self.entry.pack(fill='x', padx=12, pady=(12, 8))

        self.btn = tk.Button(self, text='Type in 5s', command=self.on_click)
        self.btn.pack(pady=(0, 8))

        self.status = tk.Label(self, text='', fg='#555')
        self.status.pack()

    def on_click(self):
        if pyautogui is None:
            messagebox.showerror('Missing dependency', 'pyautogui is required. Install with: pip install pyautogui')
            return

        text = self.entry.get()
        if not text:
            messagebox.showwarning('Empty', 'Type something in the field first.')
            return

        # disable button to avoid double-start
        self.btn.config(state='disabled')
        self.status.config(text='Waiting 5 seconds... Switch to the target input')

        def worker():
            try:
                run_typing(text, delay=5)
                self.after(0, lambda: self.status.config(text='Done'))
            except Exception as e:
                self.after(0, lambda: self.status.config(text=f'Error: {e}'))
            finally:
                self.after(0, lambda: self.btn.config(state='normal'))

        threading.Thread(target=worker, daemon=True).start()


if __name__ == '__main__':
    app = SimpleTyper()
    app.mainloop()