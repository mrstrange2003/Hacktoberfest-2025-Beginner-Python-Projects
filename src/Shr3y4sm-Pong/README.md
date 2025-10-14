# Pong Game

A classic Pong game implementation using Python and Pygame. Play against an AI opponent in this timeless arcade game!

## Features

- **Classic Pong Gameplay**: Control your paddle with arrow keys and try to score against the AI
- **AI Opponent**: Intelligent computer opponent that follows the ball
- **Score Tracking**: First to 5 points wins the game
- **Smooth Graphics**: 60 FPS gameplay with clean, minimalist design
- **Game Over Screen**: Displays winner and automatically exits after 3 seconds

## How to Play

1. Run the game using `python pong_game.py`
2. Use the **UP** and **DOWN** arrow keys to control your paddle (right side)
3. Try to hit the ball past the AI opponent's paddle (left side)
4. First player to reach 5 points wins!

## Controls

- **↑ Arrow Key**: Move paddle up
- **↓ Arrow Key**: Move paddle down
- **ESC** or **Close Window**: Quit the game

## Installation

1. Make sure you have Python 3.6+ installed
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Game

```bash
python pong_game.py
```

## Game Rules

- The ball bounces off the top and bottom walls
- When the ball goes past a paddle, the opponent scores a point
- The ball speed increases slightly after each paddle hit
- First to 5 points wins the game
- The game automatically ends and displays the winner

## Technical Details

- **Language**: Python 3
- **Graphics Library**: Pygame
- **Screen Resolution**: 980x660 pixels
- **Frame Rate**: 60 FPS
- **Ball Speed**: 7 pixels per frame
- **Paddle Speed**: 7 pixels per frame

## Requirements

- Python 3.6 or higher
- Pygame library

## File Structure

```
Pong/
├── pong_game.py      # Main game file
├── requirements.txt  # Python dependencies
└── README.md        # This file
```

Enjoy playing Pong! 🏓
