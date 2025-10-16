# Flappy-style Jumper (Shr3y4sm-Flappy)

A minimal Flappy-style jumper implemented with the Python standard library (tkinter).

Features
- Click or press Space to flap
- Procedurally spawned pipe obstacles
- Simple gravity/velocity physics
- Score counting and restart on game over

Files
- `gui_game.py` - Main game implementation using `tkinter`.
- `run.py` - Utility launcher; can optionally start the Flappy game using `--launch flappy`.

Run

1. From the folder containing `gui_game.py` (this folder):

```bash
python gui_game.py
```

2. Or use the launcher script to only start the game:

```bash
python run.py --launch flappy
```

Requirements

- The game itself uses only the Python standard library. `tkinter` is required for the GUI.

Notes on tkinter
- On many systems, `tkinter` is included with the system Python. If you get an ImportError for `tkinter`, install the appropriate package for your OS (for example, on Debian/Ubuntu: `sudo apt-get install python3-tk`).
- On Windows, the official Python installer typically includes tkinter.


Enjoy! Feel free to extend the game (graphics, sound, difficulty, or mobile-friendly controls).
