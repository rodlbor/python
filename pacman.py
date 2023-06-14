import random
import os

# Constants
EMPTY = " "
WALL = "#"
PACMAN = "C"
GHOST = "G"
DOT = "*"
POWER_PELLET = "o"

# Game state
maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '#'],
    ['#', 'C', '#', '#', '#', '#', '#', '#', '#', 'G', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
]
pacman_position = (1, 1)
ghost_position = (2, 9)
score = 0

# Helper functions
def print_maze():
    os.system("clear")  # Clear the console
    for row in maze:
        print("".join(row))

def move_pacman(direction):
    x, y = pacman_position
    dx, dy = direction
    new_x, new_y = x + dx, y + dy
    if maze[new_x][new_y] != WALL:
        if maze[new_x][new_y] == DOT:
            global score
            score += 1
        elif maze[new_x][new_y] == POWER_PELLET:
            score += 5
            # Additional power pellet logic here
        maze[x][y] = EMPTY
        maze[new_x][new_y] = PACMAN
        pacman_position = (new_x, new_y)

def move_ghost():
    x, y = ghost_position
    dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
    new_x, new_y = x + dx, y + dy
    if maze[new_x][new_y] != WALL:
        maze[x][y] = EMPTY
        maze[new_x][new_y] = GHOST
        ghost_position = (new_x, new_y)

# Main game loop
while True:
    print_maze()
    print(f"Score: {score}")
    print("Use 'w' for up, 's' for down, 'a' for left, 'd' for right")
    move = input("Enter your move: ")

    if move == "w":
        move_pacman((-1, 0))
    elif move == "s":
        move_pacman((1, 0))
    elif move == "a":
        move_pacman((0, -1))
    elif move == "d":
        move_pacman((0, 1))

    move_ghost()
