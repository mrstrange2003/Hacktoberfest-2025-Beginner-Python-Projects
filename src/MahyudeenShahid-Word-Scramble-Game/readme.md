# Word Scramble — MahyudeenShahid

An interactive, beginner-friendly CLI Word Scramble game with categories, hints, streak/combo bonuses, time-based scoring, and persistent high scores and stats.

## Features

- Difficulty levels: `easy`, `medium`, `hard` (affects rounds, word length, time limits)
- Categories (mix or pick a category like `programming`)
- Hint command during a round to reveal a letter
- Skip and Quit commands for control
- Time-based scoring with difficulty multipliers
- Streak/combo bonuses for consecutive correct answers
- Persistent top-10 high scores saved to `high_scores.json`
- Simple player stats saved to `stats.json` (games played, best streak)
- No external dependencies — runs on Python 3.8+

## Run locally (Windows)

1. Open PowerShell and change directory to the project folder:

```powershell
cd e:\hacktoberfest\beginner-python-mini-projects-hacktoberfest-2025\src\MahyudeenShahid-Word-Scramble-Game
```

2. Run the game:

```powershell
python main.py
```

You will see a menu. Choose `Play` and follow the prompts.

## Files

- `main.py` — game implementation (entry point)
- `README.md` — this file
- `high_scores.json` — created automatically when first high score is saved
- `stats.json` — created automatically to track simple stats

## Available categories

- general (mixed words)
- programming (e.g. python, function, module)
- networking (e.g. network, protocol)
- animals (e.g. elephant, tiger, penguin, dolphin)
- movies (e.g. inception, titanic, interstellar, matrix)
- foods (e.g. pizza, sushi, lasagna, cupcake)

## Gameplay Commands

- During a round:
   - Type your guess and press Enter
   - `hint` — reveals a letter in the correct position
   # Word Scramble — MahyudeenShahid

   Professional, well-documented CLI Word Scramble game built for beginners and contributors.

   This repository contains a compact, dependency-free Python project that demonstrates clean code, persistent data, and a few gameplay mechanics useful for learning and quick contributions.

   ## Table of Contents

   - Overview
   - Tech stack
   - Quick start
   - Usage & gameplay
   - Scoring and mechanics
   - Data files (high scores & stats)
   - Contributing
   - Testing
   - Troubleshooting
   - License & Contact

   ## Overview

   Word Scramble is a command-line game where players guess the original word from a scrambled version. The game supports difficulty levels, multiple categories, hints, streak bonuses, and persistent leaderboards.

   ## Tech stack

   - Python 3.8+
   - Standard library only (no external dependencies)
   - JSON for simple persistent storage (`high_scores.json`, `stats.json`)

   ## Quick start

   1. Open PowerShell and navigate to the project folder:

   ```powershell
   cd e:\hacktoberfest\beginner-python-mini-projects-hacktoberfest-2025\src\MahyudeenShahid-Word-Scramble-Game
   ```

   2. Run the game:

   ```powershell
   python main.py
   ```

   3. From the main menu choose `Play` and follow the prompts.

   ## Usage & gameplay

   - Main menu options: Play, Show High Scores, About/Instructions, Quit.
   - Play flow:
      1. Choose difficulty: `easy`, `medium`, or `hard`.
      2. Pick a category (or press Enter for mixed words). Available categories include `general`, `programming`, `networking`, `animals`, `movies`, `foods`.
      3. Each round displays a scrambled word. Commands available during a round:
          - Type your guess and press Enter
          - `hint` — reveals a single letter in its correct position
          - `skip` — skip the current word (no points)
          - `quit` — end the game immediately

   ## Scoring and mechanics

   - Base score: `len(word) * 10`.
   - Difficulty multiplier: `easy`=1.0, `medium`=1.5, `hard`=2.0.
   - Time bonus: up to +20 points scaled by how quickly the player answers (faster = more bonus).
   - Streak/Combo bonus: +5% of the round points for each consecutive correct answer after the first (rounded down).

   Example: guessing a 6-letter word on `medium` quickly could yield: `6*10*1.5 + time_bonus + combo_bonus`.

   ## Data files

   - `high_scores.json`: saved top-10 leaderboard entries, created automatically when first score qualifies.
   - `stats.json`: lightweight player stats (e.g., games_played, best_streak), created/updated automatically.

   Sample `high_scores.json` entry:

   ```json
   [
      {
         "name": "Alice",
         "score": 420,
         "date": "2025-10-21 12:00 UTC"
      }
   ]
   ```

   Sample `stats.json`:

   ```json
   {
      "games_played": 3,
      "best_streak": 4
   }
   ```

   ## Contributing

   Recommended small contributions for quick PRs:

   - Add or expand categories (place large lists in a `data/` folder as JSON files).
   - Add unit tests for `scramble_word`, `compute_score`, and category loading.
   - Add more helpful CLI output, e.g., colored banners, stats summary after each game.

   When opening a PR, keep changes focused to a single folder, include a short README update if you add data, and add a small test or example run output if possible.

   ## Testing

   You can test functions locally (suggested approach):

   - Run `python -c "import main; print(main.scramble_word('python'))"` to see scrambled output.
   - Add `pytest` tests under `tests/` for CI-friendly validation (not required for this repo).

   ## Troubleshooting

   - If colors don't render on Windows `cmd.exe`, try PowerShell or Windows Terminal.
   - If a JSON file becomes corrupted, delete `high_scores.json` / `stats.json` and they will be recreated.

   ## License

    MIT

    Enjoy — open a PR if you add categories, tests, or polish!

   ---

   👨‍💻 Developed with ❤️ by [Mahyudeen Shahid](https://github.com/MahyudeenShahid)