## Code-Roast-or-Compliment

A Fun CLI Project that randomly teases your Python code. Perfect for developers who loves humour while coding.

## Features

- Random roasts to tease your code
- Random Compliments to boost your confidence
- Fully terminal based, lightweight and beginner friendly
- Colors and emojis added for a lively experience

## Requirements

- Python 3.x 
- colorama library for colored terminal output

Install colorama using pip :

```bash
   pip install colorama
```
⚠️ If you get "externally managed environment" errors on Linux/Mac, consider using a virtual environment.

## Virtual Environment Setup (Optional)

Using a virtual environment ensures dependencies like colorama don’t conflict with system Python.

Linux :

```bash
   python3 -m venv venv        # create a virtual environment named 'venv'
   source venv/bin/activate    # activate it
   pip install colorama        # install requirements inside the environment
```
Windows:

``` bash
    python -m venv venv
    venv\Scripts\activate
    pip install colorama
```
- Your terminal will show <b>(venv)</b> when the virtual environment is active

- To Deactivate it, type
```bash 
    deactivate
```

## How to Run

```bash 
   python3 main.py
```

<b> 1. Choose Selection :</b>
- r  -> roasts
- c  -> compliments
- s  -> surprise

<b> 2. Analyze Python File:</b>

- y → Enter a Python file (must be in the same folder) to get fun code insights.
- n → Skip code analysis (the program exits with a fun message).

<b> 3. Result:</b>
- Roast/compliment messages is printed with colors and emojis.

- Optional code insight if a Python file is analyzed.

Note : ⚠️ If the file you enter does not exist, the program will show a friendly "File Not Found!" message and exit.

## Output
``` bash

💻 Welcome to the Code-Roast-or-Compliment 💻
Because your code deserves feedback... even if it didn’t ask for it 😅

Choose mode (r = Roast, c = Compliment, s = Surprise :) c
😎 Want to analyze your python code just for fun? (y/n) y
📁 Input your Python file here : main.py

📝 Result:

🤓 you wrote that logic? that’s surprisingly neat 💖

🔍 Code Insight : So many lines of code, maybe you wrote an entire framework !!

🎮 Thanks for playing Code-Roast-or-Compliment 💻💖

```


## Notes
- All roasts and compliments are in data.json, you can add your own!

- The program is CLI based and does not require a internet connection

---

