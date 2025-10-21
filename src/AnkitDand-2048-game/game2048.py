import random
import os
import sys


class Game2048:
    def __init__(self, size=6):
        self.size = size
        self.score = 0
        self.board = [[0] * size for _ in range(size)]
        self.add_tile()
        self.add_tile()

    def add_tile(self):
        empty_cells = [(r, c) for r in range(self.size)
                       for c in range(self.size) if self.board[r][c] == 0]
        if not empty_cells:
            return
        r, c = random.choice(empty_cells)
        self.board[r][c] = random.choice([2, 4])

    def print_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("🎮 2048 Game | Score:", self.score)
        print("-" * (self.size * 8))
        for row in self.board:
            for cell in row:
                print(f"{cell or '.':^8}", end="")
            print("\n")
        print("-" * (self.size * 8))
        print("Use W/A/S/D to move | Q to quit\n")

    def compress(self, row):
        """Move all non-zero elements to the left."""
        new_row = [num for num in row if num != 0]
        new_row += [0] * (self.size - len(new_row))
        return new_row

    def merge(self, row):
        """Merge identical adjacent tiles."""
        for i in range(self.size - 1):
            if row[i] != 0 and row[i] == row[i + 1]:
                row[i] *= 2
                self.score += row[i]
                row[i + 1] = 0
        return self.compress(row)

    def move_left(self):
        moved = False
        new_board = []
        for row in self.board:
            compressed = self.compress(row)
            merged = self.merge(compressed)
            new_board.append(merged)
            if merged != row:
                moved = True
        self.board = new_board
        return moved

    def move_right(self):
        self.board = [list(reversed(row)) for row in self.board]
        moved = self.move_left()
        self.board = [list(reversed(row)) for row in self.board]
        return moved

    def transpose(self):
        self.board = [list(row) for row in zip(*self.board)]

    def move_up(self):
        self.transpose()
        moved = self.move_left()
        self.transpose()
        return moved

    def move_down(self):
        self.transpose()
        moved = self.move_right()
        self.transpose()
        return moved

    def is_game_over(self):
        # Check if there are any empty cells
        for row in self.board:
            if 0 in row:
                return False
        # Check possible merges
        for r in range(self.size):
            for c in range(self.size - 1):
                if self.board[r][c] == self.board[r][c + 1]:
                    return False
        for c in range(self.size):
            for r in range(self.size - 1):
                if self.board[r][c] == self.board[r + 1][c]:
                    return False
        return True

    def has_won(self):
        return any(2048 in row for row in self.board)


def main():
    game = Game2048()
    while True:
        game.print_board()
        if game.has_won():
            print("🎉 Congratulations! You reached 2048!")
            break
        if game.is_game_over():
            print("💀 Game Over! No moves left.")
            break

        move = input("Move (W/A/S/D or Q): ").lower()
        if move == 'q':
            print("👋 Thanks for playing!")
            sys.exit()
        elif move == 'w':
            moved = game.move_up()
        elif move == 's':
            moved = game.move_down()
        elif move == 'a':
            moved = game.move_left()
        elif move == 'd':
            moved = game.move_right()
        else:
            print("❌ Invalid move! Use only W/A/S/D.")
            input("Press Enter to continue...")
            continue

        if moved:
            game.add_tile()


if __name__ == "__main__":
    main()
