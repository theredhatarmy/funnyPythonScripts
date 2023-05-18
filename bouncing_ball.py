import random
import time

# ASCII art frames
frames = [
    r"   ___   ",
    r"  /   \  ",
    r" |     | ",
    r"  \___/  ",
    r"         ",
]

# Generate random colors
colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m', '\033[97m']

# Function to clear the console screen
def clear_screen():
    print("\033c", end="")

# Function to randomly select a color
def select_color():
    return random.choice(colors)

# Main animation loop
def animate():
    clear_screen()

    # Initial position
    x = 0
    y = 0

    # Initial direction
    dx = 1
    dy = 1

    # Randomly select a color for the ball
    color = select_color()

    while True:
        clear_screen()

        # Update the position
        x += dx
        y += dy

        # Reverse direction if hitting the screen boundaries
        if x <= 0 or x >= len(frames[0]) - 1:
            dx *= -1
            color = select_color()

        if y <= 0 or y >= len(frames) - 1:
            dy *= -1
            color = select_color()

        # Print the ball at the current position
        for i, line in enumerate(frames):
            if i == y:
                print(" " * x + color + line + "\033[0m")
            else:
                print(line)

        # Pause for a while
        time.sleep(0.1)

# Start the animation
animate()
