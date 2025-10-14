import pygame
import sys
import random

# Simple single-file Pong game using Pygame.
#
# This script creates a window, draws paddles and a ball, and implements
# basic collision, scoring, and a lightweight AI opponent.

def ball_animations():
    """Update ball position, handle wall/paddle collisions, and scoring.

    - Moves the ball by its current velocity
    - Bounces off top/bottom screen edges
    - Detects when the ball passes left/right edges and updates scores
    - Restarts the rally or ends the game when someone reaches 5
    """
    global ball_speed_x, ball_speed_y, player_score, opponent_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0:
        player_score += 1
        if player_score >= 5:
            display_winner("You have won!!!")
        else:
            ball_restart()
    if ball.right >= screen_width:
        opponent_score += 1
        if opponent_score >= 5:
            display_winner("YOU LOST!!!")
        else:
            ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    """Move the player paddle and clamp it within the screen."""
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_ai():
    """Very simple AI: move the opponent paddle toward the ball's y position."""
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_restart():
    """Recenter the ball and randomly flip its direction on both axes."""
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))

def display_winner(winner):
    """Render a winner message, pause briefly, then exit the game."""
    font = pygame.font.Font(None, 100)
    text = font.render(f"{winner}", True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen_width/2, screen_height/2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.delay(3000)  # Display winner for 3 seconds before quitting
    pygame.quit()
    sys.exit()

# # Get player's name
# player_name = input("Enter your name: ")

# --- Basic Setup ---
pygame.init()
clock = pygame.time.Clock()

# --- Display / Window ---
screen_width = 980
screen_height = 660
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# --- Game Entities (Rectangles) ---
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

# Colors
bg_color = pygame.Color("grey12")
lightgrey = (200, 200, 200)

# Movement speeds (pixels per frame)
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0  # updated by key events
opponent_speed = 7

# --- Scoring ---
player_score = 0
opponent_score = 0
score_font = pygame.font.SysFont('Century Gothic', 70)

# --- Main Game Loop ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball_animations()
    player_animation()
    opponent_ai()

    # --- Rendering ---
    screen.fill(bg_color)
    pygame.draw.rect(screen, lightgrey, player)
    pygame.draw.rect(screen, lightgrey, opponent)
    pygame.draw.ellipse(screen, lightgrey, ball)
    pygame.draw.aaline(screen, lightgrey, (screen_width/2, 0),(screen_width/2, screen_height))

    # Scores HUD
    player_text = score_font.render(str(player_score), True, lightgrey)
    screen.blit(player_text, (screen_width/2 + 40, 50))
    opponent_text = score_font.render(str(opponent_score), True, lightgrey)
    screen.blit(opponent_text, (screen_width/2 - 60, 50))

    pygame.display.flip()
    clock.tick(60)
