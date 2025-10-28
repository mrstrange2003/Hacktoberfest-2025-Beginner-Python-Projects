import random

def create_board(rows, cols, num_mines):
    """Creates the game board with mines and adjacent mine counts."""
    board = [[' ' for _ in range(cols)] for _ in range(rows)]
    mines = set()

    # Place mines
    while len(mines) < num_mines:
        r, c = random.randint(0, rows - 1), random.randint(0, cols - 1)
        if (r, c) not in mines:
            mines.add((r, c))
            board[r][c] = '*' # Mark mine

    # Calculate adjacent mine counts
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == '*':
                continue
            count = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == '*':
                        count += 1
            if count > 0:
                board[r][c] = str(count)
    return board, mines

def display_board(player_board):
    """Prints the player's view of the board."""
    for row in player_board:
        print(' '.join(row))

def reveal_cell(board, player_board, r, c, rows, cols):
    """Recursively reveals cells and updates player's view."""
    if not (0 <= r < rows and 0 <= c < cols) or player_board[r][c] != '#':
        return

    player_board[r][c] = board[r][c]

    if board[r][c] == ' ': # If empty, reveal neighbors
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                reveal_cell(board, player_board, r + dr, c + dc, rows, cols)

def play_minesweeper():
    rows, cols = 5, 5
    num_mines = 5
    board, mines = create_board(rows, cols, num_mines)
    player_board = [['#' for _ in range(cols)] for _ in range(rows)] # '#' for unrevealed

    game_over = False
    while not game_over:
        display_board(player_board)
        try:
            action = input("Enter 'r' to reveal or 'f' to flag, then row and col (e.g., r 0 0): ").split()
            cmd = action[0].lower()
            r, c = int(action[1]), int(action[2])

            if cmd == 'r':
                if (r, c) in mines:
                    print("BOOM! Game Over.")
                    game_over = True
                    display_board(board) # Show full board
                else:
                    reveal_cell(board, player_board, r, c, rows, cols)
            elif cmd == 'f':
                if player_board[r][c] == '#':
                    player_board[r][c] = 'F' # Flagged
                elif player_board[r][c] == 'F':
                    player_board[r][c] = '#' # Unflag
            else:
                print("Invalid command. Use 'r' or 'f'.")

            # Check win condition
            revealed_count = sum(row.count(' ') + sum(1 for cell in row if cell.isdigit()) for row in player_board)
            if revealed_count == (rows * cols) - num_mines:
                print("Congratulations! You won!")
                game_over = True

        except (ValueError, IndexError):
            print("Invalid input. Please use the format 'r row col' or 'f row col'.")

if __name__ == "__main__":
    play_minesweeper()