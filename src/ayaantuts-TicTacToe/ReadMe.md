# Python Tic-Tac-Toe
This project is a classic command-line implementation of the game Tic-Tac-Toe, written in Python. It features a clean, object-oriented design that separates the game logic from the player logic, allowing for easy extension and modification. You can play as 'X' against a simple computer opponent that chooses its moves randomly.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
	- [Prerequisites](#prerequisites)
	- [How to Play](#how-to-play)
- [Code Overview](#code-overview)
	- [`player.py`](#playerpy)
	- [`tictactoe.py`](#tictactoepy)

## Features
  - **Human vs. Computer Gameplay**: Play against a simple AI that makes random moves.
  - **Object-Oriented Design**: The code is structured into `TicTacToe` and `Player` classes, making it readable and scalable.
  - **Clear CLI**: An intuitive command-line interface shows the board and prompts for user input.
  - **Input Validation**: The game handles invalid inputs gracefully, prompting the user to try again.
  - **Modular Code**: Game logic (`tictactoe.py`) and player logic (`player.py`) are in separate files for better organization.

## Getting Started
### Prerequisites
You need to have **Python 3** installed on your system. No external libraries are required, as the project only uses the built-in `random` and `time` modules.

### How to Play
1.  **Clone or Download**: Get the source code and place both `player.py` and `tictactoe.py` in the same directory.

2.  **Run the Game**: Open your terminal or command prompt, navigate to the directory where you saved the files, and run the main game file:

    ```sh
    python tictactoe.py
    ```

3.  **Make Your Move**: The game will start by printing a numbered reference board. When it's your turn ('X'), simply type the number (0-8) corresponding to the square you want to play and press Enter.

    The game will continue until there is a winner or a tie.

-----

## Code Overview
The project is split into two main files:

### `player.py`
This file defines the different types of players in the game. It uses a base `Player` class and subclasses for different behaviors.
  - **`Player` (Base Class)**
	- This is an abstract class that all other players inherit from.
	- It initializes a player with a letter ('X' or 'O').
	- It contains a `get_move()` method that subclasses must implement.

  - **`HumanPlayer`**
	- Inherits from `Player`.
	- Implements `get_move()` by prompting the user for input via the command line.
	- Includes validation to ensure the input is a number corresponding to a valid, available square on the board.

  - **`RandomComputerPlayer`**
	- Inherits from `Player`.
	- Implements `get_move()` by selecting a random move from the list of available squares provided by the game instance.

### `tictactoe.py`
This file contains the game engine and the main script to run the game.
- **`TicTacToe` (Class)**
	- **`__init__()`**: Initializes the game board as a list of 9 empty spaces.
	- **`print_board()`**: Prints the current state of the board.
	- **`print_board_nums()`**: A static method that prints the numbered reference board for the player.
	- **`available_moves()`**: Returns a list of indices for the empty squares.
	- **`make_move(square, letter)`**: Places a player's letter on the board and checks if that move resulted in a win.
	- **`winner(square, letter)`**: The core win-checking logic. After a move is made, it efficiently checks only the relevant row, column, and diagonals to see if the current player has won.

- **`play(game, x_player, o_player, print_game=True)` (Function)**
	- This is the main game loop that orchestrates the entire game.
	- It takes a game instance and two player instances as input.
	- It alternates turns between 'X' and 'O', calling the appropriate player's `get_move()` method.
	- After each move, it prints the board, checks for a winner, and handles the game-over conditions (win or tie).