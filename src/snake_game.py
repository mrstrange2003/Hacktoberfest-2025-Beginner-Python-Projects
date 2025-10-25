import pygame
import random
import os
import sys

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
CELL_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // CELL_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // CELL_SIZE

FPS_INITIAL = 8
SPEED_INCREMENT_EVERY = 5
SPEED_INCREASE = 1

SNAKE_COLOR = (0, 200, 0)
FOOD_COLOR = (200, 0, 0)
BG_COLOR = (0, 0, 0)
GRID_COLOR = (20, 20, 20)
TEXT_COLOR = (180, 180, 180)

HIGHSCORE_FILE = "highscore.txt"

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def load_highscore():
    if not os.path.exists(HIGHSCORE_FILE):
        with open(HIGHSCORE_FILE, "w") as f:
            f.write("0")
        return 0
    try:
        with open(HIGHSCORE_FILE, "r") as f:
            return int(f.read().strip() or 0)
    except:
        return 0

def save_highscore(score):
    try:
        with open(HIGHSCORE_FILE, "w") as f:
            f.write(str(score))
    except:
        pass

def draw_block(surface, color, pos):
    x, y = pos
    rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(surface, color, rect)

def random_food_position(snake):
    positions = [(x, y) for x in range(GRID_WIDTH) for y in range(GRID_HEIGHT)]
    free = list(set(positions) - set(snake))
    return random.choice(free)

def draw_grid(surface):
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(surface, GRID_COLOR, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
        pygame.draw.line(surface, GRID_COLOR, (0, y), (WINDOW_WIDTH, y))

def show_text_center(surface, text, font, color, y_offset=0):
    text_surf = font.render(text, True, color)
    rect = text_surf.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + y_offset))
    surface.blit(text_surf, rect)

def game_loop(screen, clock, big_font, small_font):
    start_x = GRID_WIDTH // 2
    start_y = GRID_HEIGHT // 2
    snake = [(start_x, start_y), (start_x - 1, start_y), (start_x - 2, start_y)]
    direction = RIGHT
    next_direction = RIGHT
    food = random_food_position(snake)
    score = 0
    fps = FPS_INITIAL
    highscore = load_highscore()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != DOWN:
                    next_direction = UP
                elif event.key == pygame.K_DOWN and direction != UP:
                    next_direction = DOWN
                elif event.key == pygame.K_LEFT and direction != RIGHT:
                    next_direction = LEFT
                elif event.key == pygame.K_RIGHT and direction != LEFT:
                    next_direction = RIGHT
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        direction = next_direction
        head_x, head_y = snake[0]
        dx, dy = direction
        new_head = ((head_x + dx) % GRID_WIDTH, (head_y + dy) % GRID_HEIGHT)

        if new_head in snake:
            if score > highscore:
                highscore = score
                save_highscore(highscore)
            return score, highscore

        snake.insert(0, new_head)

        if new_head == food:
            score += 1
            if score % SPEED_INCREMENT_EVERY == 0:
                fps += SPEED_INCREASE
            food = random_food_position(snake)
        else:
            snake.pop()

        screen.fill(BG_COLOR)
        draw_grid(screen)
        draw_block(screen, FOOD_COLOR, food)
        for segment in snake:
            draw_block(screen, SNAKE_COLOR, segment)

        score_surf = small_font.render(f"Score: {score}", True, TEXT_COLOR)
        hs_surf = small_font.render(f"High: {highscore}", True, TEXT_COLOR)
        screen.blit(score_surf, (8, 8))
        screen.blit(hs_surf, (WINDOW_WIDTH - hs_surf.get_width() - 8, 8))

        pygame.display.flip()
        clock.tick(fps)

def game_over_screen(screen, clock, big_font, small_font, last_score, highscore):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                return

        screen.fill(BG_COLOR)
        show_text_center(screen, "GAME OVER", big_font, TEXT_COLOR, -40)
        show_text_center(screen, f"Score: {last_score} High: {highscore}", small_font, TEXT_COLOR, 0)
        show_text_center(screen, "Press any key to restart", small_font, TEXT_COLOR, 40)

        pygame.display.flip()
        clock.tick(10)

def main():
    pygame.init()
    pygame.display.set_caption("Retro Snake")
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    small_font = pygame.font.SysFont("consolas", 18)
    big_font = pygame.font.SysFont("consolas", 48)
    load_highscore()

    while True:
        last_score, highscore = game_loop(screen, clock, big_font, small_font)
        game_over_screen(screen, clock, big_font, small_font, last_score, highscore)

if __name__ == "__main__":
    main()

