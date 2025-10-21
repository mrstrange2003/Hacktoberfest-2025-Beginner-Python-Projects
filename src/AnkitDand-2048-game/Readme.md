## 🧩 2048 Game (Python CLI)

A terminal-based implementation of the classic **2048 puzzle game**, built entirely in **Python**.
The game uses simple keyboard controls (`W`, `A`, `S`, `D`) and displays a dynamic board that updates after every move.
It follows a clean, **object-oriented design**, making it easy to read, extend, and modify.

---

### 🎮 Features

- **Classic 2048 Gameplay:** Combine tiles to reach the 2048 tile and win.
- **Dynamic Board:** Supports flexible grid sizes (default 6×6).
- **Score Tracking:** Keeps track of your score as tiles merge.
- **CLI Interface:** Simple, text-based board that refreshes every move.
- **Input Validation:** Handles invalid inputs gracefully.
- **Easy to Extend:** Modify tile size, win conditions, or colors easily.

---

### ⚙️ Getting Started

#### 🧠 Prerequisites

- Python 3.x installed
- No external libraries required (`random` and `os` are built-in)

#### 🚀 How to Run

1. Clone or download this repository.
2. Open a terminal and navigate to the project folder:

   ```bash
   cd src/AnkitDand-2048-game
   ```

3. Run the game:

   ```bash
   python game2048.py
   ```

---

### 🎯 How to Play

- Use the following keys to move the tiles:

  ```
  W → Move Up
  A → Move Left
  S → Move Down
  D → Move Right
  Q → Quit Game
  ```

- When two tiles with the same number touch, they merge into one!
- Keep merging until you create the **2048 tile** 🎉
- The game ends when:

  - No more moves are possible (Game Over 💀), or
  - You reach 2048 (You Win 🎉)

---

### 🧩 Code Overview

#### `Game2048` Class

Handles:

- **Board initialization**
- **Tile movement and merging**
- **Score updates**
- **Game over and win detection**
- **Board printing and input handling**

#### Key Methods

| Method                                                 | Description                                   |
| ------------------------------------------------------ | --------------------------------------------- |
| `add_tile()`                                           | Adds a new 2 or 4 tile at a random empty spot |
| `move_left() / move_right() / move_up() / move_down()` | Handles tile movements and merging            |
| `is_game_over()`                                       | Checks if no more moves are possible          |
| `has_won()`                                            | Checks if the player reached 2048             |

---
