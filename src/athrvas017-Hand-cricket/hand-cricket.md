# 🏏 Hand Cricket Game

A simple, command-line implementation of the classic Indian "Hand Cricket" game written in Python. This is a single-player game where the user bats against the computer's bowling.

---

## 🚀 Features

* **Custom Overs:** The user can specify the number of overs for the match.
* **Simple Gameplay:** Easy-to-understand rules based on matching numbers.
* **Scorecard:** Prints a detailed ball-by-ball scorecard and final statistics.
* **Valid Runs:** Players can score 0, 1, 2, 4, or 6 runs.
* **2 Wicket Limit:** The innings ends after the batsman loses 2 wickets.

---

## 💻 How to Run

### Prerequisites

You only need **Python 3** installed on your system.

### Running the Script

1.  Save the provided code as a Python file (e.g., `hand_cricket.py`).
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you saved the file.
4.  Run the game using the following command:

    ```bash
    python hand_cricket.py
    ```

5.  The game will start by asking you to input the number of overs you wish to play.

---

## 🎮 How to Play

### Batting Rules

1.  **Start:** The game will prompt you to enter the number of overs. The total balls will be calculated (Overs * 6).
2.  **Choose Your Shot:** When prompted, enter your batting choice (runs) from the valid list: **`0, 1, 2, 4, 6`**.
3.  **Computer's Turn (Bowler):** The computer will randomly choose a number from the same list.
4.  **Scoring:**
    * If your chosen run **DOES NOT MATCH** the computer's run, your chosen run is added to your **score**.
    * If your chosen run **MATCHES** the computer's run, you are **OUT!** and you lose a **wicket**.
5.  **Innings End:** Your innings ends when one of the following conditions is met:
    * You lose **2 wickets**.
    * The total number of balls (calculated from the overs you chose) has been bowled.

### Example Gameplay