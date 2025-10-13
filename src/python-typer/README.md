Simple Beginner Typer

This is a minimal beginner-friendly utility with a single text field and a single button.

Behavior:
- Enter text in the field.
- Click the "Type in 5s" button.
- The app waits 5 seconds (use this time to focus the target input), then types the entered text into the currently focused field.

Files:
- `typer.py` - the main minimal GUI script.
- `requirements.txt` - python dependencies (only `pyautogui`).

Usage (Windows PowerShell):
1. Change to the folder:

```powershell
cd 'd:\{your-dir}\Whatsapp-Message-Generator\python-typer'
```

2. (Optional) Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependency:

```powershell
pip install -r requirements.txt
```

4. Run the app:

```powershell
python typer.py
```

Notes:
- Make sure the target input (where you want text typed) is focused before the 5-second countdown ends.
- Use responsibly; this program simulates keystrokes.