# Hangman Game in Python

A simple command-line Hangman game implemented in Python. Guess the letters of a randomly selected word before running out of lives!

## Features
- Random word selection from a file (`words.txt`)
- Visual representation of hangman stages
- Tracks already guessed letters
- Input validation and case-insensitive guessing
- Continuous play until user exits

## Installation
1. Clone the repository.
2. Make sure you have Python 3 installed.
3. Add a words.txt file in the same directory with a list of words (one word per line).

## Usage

- Run the program using: hangman.py
- Follow the on-screen prompts to guess letters and try to save the hangman!

## Example
-------------Welcome to Hangman-------------

Guess the word:-  _ _ _ _ _
Lives: 6
Guess a Letter: a
_ a _ _ _
Lives: 6

## Notes
- The game will show a hangman diagram for each incorrect guess.
- You can play repeatedly until you choose to exit.