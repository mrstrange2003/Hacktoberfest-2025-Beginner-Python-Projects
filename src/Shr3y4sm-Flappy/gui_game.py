"""Simple Flappy-style jumper implemented with tkinter.

This module provides a minimal Flappy-like game with:
- Click or Space to flap
- Procedurally spawned pipes
- Simple physics (gravity and velocity)
- Score counting and restart on game over

It's intentionally compact and easy to read/extend.
"""

import tkinter as tk
import random
import time


class FlappyBirdSimple:
    """Main game application class.

    Attributes:
        root: tk.Tk main window reference.
        canvas: drawing surface for the game.
        bird: canvas item id for the player bird.
        pipes: list of tuples holding (top_pipe_id, bottom_pipe_id).
        running: whether the game loop is active.
    """
    def __init__(self, root):
        self.root = root
        self.width = 400
        self.height = 600
        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg="#87CEEB")
        self.canvas.pack()

        # Bird
        self.bird_size = 20
        self.bird_x = 80
        self.bird_y = self.height // 2
        self.bird = self.canvas.create_oval(self.bird_x - self.bird_size//2,
                                            self.bird_y - self.bird_size//2,
                                            self.bird_x + self.bird_size//2,
                                            self.bird_y + self.bird_size//2,
                                            fill="yellow", outline="orange")

        # Game physics parameters
        self.gravity = 0.55
        self.velocity = 0
        self.flap_strength = -9

        # Pipe configuration
        self.pipe_width = 60
        self.pipe_gap = 150
        self.pipe_speed = 3
        self.pipes = []  # list of tuples (top_id, bottom_id)
        self.pipe_interval = 1500  # milliseconds

        # Score
        self.score = 0
        self.score_text = self.canvas.create_text(self.width//2, 30, text=f"Score: {self.score}",
                                                  font=("Helvetica", 18), fill="white")

        # Game state
        self.running = True
        self.game_over_text = None

        # Bind keyboard and mouse controls to the flap action
        # Use self.root so bindings remain correct if root reference changes
        self.root.bind('<space>', self.flap)
        self.root.bind('<Button-1>', self.flap)

        # Start
        self.last_pipe_time = 0
        self.spawn_pipe()
        self.update()

    def flap(self, event=None):
        """Apply an upward impulse to the bird.

        If the game has ended, flap will trigger a reset so the user can restart
        by pressing Space or clicking.
        """
        if not self.running:
            self.reset()
            return
        # Set an immediate upward velocity
        self.velocity = self.flap_strength

    def spawn_pipe(self):
        """Create a new pipe pair off the right edge and schedule the next spawn."""
        gap_y = random.randint(120, self.height - 120 - self.pipe_gap)
        x = self.width + self.pipe_width
        # Top pipe (from top of screen down to gap start)
        top = self.canvas.create_rectangle(x, 0, x + self.pipe_width, gap_y, fill="#228B22", outline="")
        # Bottom pipe (from gap end down to bottom of screen)
        bottom = self.canvas.create_rectangle(x, gap_y + self.pipe_gap, x + self.pipe_width, self.height,
                                              fill="#228B22", outline="")
        self.pipes.append((top, bottom))
        # Schedule the next pipe spawn after pipe_interval milliseconds
        self.root.after(self.pipe_interval, self.spawn_pipe)

    def update_pipes(self):
        remove = []
        for top, bottom in self.pipes:
            self.canvas.move(top, -self.pipe_speed, 0)
            self.canvas.move(bottom, -self.pipe_speed, 0)
            coords = self.canvas.coords(top)
            if coords and coords[2] < 0:
                # Pipe moved fully left off screen: schedule for removal
                remove.append((top, bottom))
                # increase score when the pipe has passed the bird's x position
                self.score += 1
                self.canvas.itemconfigure(self.score_text, text=f"Score: {self.score}")

        for pair in remove:
            top, bottom = pair
            try:
                self.canvas.delete(top)
                self.canvas.delete(bottom)
            except Exception:
                pass
            if pair in self.pipes:
                self.pipes.remove(pair)

    def check_collision(self):
        # Bird bbox
        bx1, by1, bx2, by2 = self.canvas.coords(self.bird)
        # Out of bounds
        if by1 <= 0 or by2 >= self.height:
            return True
        # Check pipes
        for top, bottom in self.pipes:
            tcoords = self.canvas.coords(top)
            bcoords = self.canvas.coords(bottom)
            if not tcoords or not bcoords:
                continue
            tx1, ty1, tx2, ty2 = tcoords
            bx1i, by1i, bx2i, by2i = bx1, by1, bx2, by2
            # Axis-aligned bounding box (AABB) collision test against top pipe
            if not (bx2i < tx1 or bx1i > tx2 or by2i < ty1 or by1i > ty2):
                return True
            # AABB check against bottom pipe
            bx1i, by1i, bx2i, by2i = bx1, by1, bx2, by2
            tx1, ty1, tx2, ty2 = bcoords
            if not (bx2i < tx1 or bx1i > tx2 or by2i < ty1 or by1i > ty2):
                return True
        return False

    def update(self):
        if not self.running:
            return

        # Physics
        self.velocity += self.gravity
        self.bird_y += self.velocity
        self.canvas.move(self.bird, 0, self.velocity)

        # Pipes
        self.update_pipes()

        # Collision
        if self.check_collision():
            self.game_over()
            return

        # Schedule next frame
        # Roughly 60 FPS: 1000ms/60 ≈ 16ms per frame
        self.root.after(16, self.update)

    def game_over(self):
        self.running = False
        # Display game over message with the final score and restart hint
        self.game_over_text = self.canvas.create_text(self.width//2, self.height//2,
                                                      text=f"Game Over\nScore: {self.score}\nClick or Space to restart",
                                                      font=("Helvetica", 20), fill="red", justify='center')

    def reset(self):
        # Clear pipes
        for top, bottom in list(self.pipes):
            try:
                self.canvas.delete(top)
                self.canvas.delete(bottom)
            except Exception:
                pass
        self.pipes.clear()
        # Reset bird
        self.canvas.coords(self.bird,
                           self.bird_x - self.bird_size//2,
                           self.height//2 - self.bird_size//2,
                           self.bird_x + self.bird_size//2,
                           self.height//2 + self.bird_size//2)
        self.bird_y = self.height // 2
        self.velocity = 0
        self.score = 0
        self.canvas.itemconfigure(self.score_text, text=f"Score: {self.score}")
        if self.game_over_text:
            self.canvas.delete(self.game_over_text)
            self.game_over_text = None
        self.running = True
        # restart spawning
        # Restart pipe spawning and the main update loop
        self.spawn_pipe()
        self.update()


def main():
    root = tk.Tk()
    root.title("Flappy-style Jumper")
    app = FlappyBirdSimple(root)
    root.mainloop()


if __name__ == '__main__':
    main()
