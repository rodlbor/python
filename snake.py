import random
import msvcrt

# Game settings
WIDTH = 20
HEIGHT = 10
SNAKE_HEAD = 'O'
SNAKE_BODY = '*'
FOOD = 'F'

# Snake directions
UP = 'w'
DOWN = 's'
LEFT = 'a'
RIGHT = 'd'

def clear_screen():
    print("\033[H\033[J")  # ANSI escape sequence to clear the screen

def get_key():
    return msvcrt.getch().decode('utf-8')

def initialize_game():
    snake_x = random.randint(1, WIDTH - 2)
    snake_y = random.randint(1, HEIGHT - 2)
    snake = [(snake_x, snake_y)]
    direction = RIGHT

    food_x = random.randint(1, WIDTH - 2)
    food_y = random.randint(1, HEIGHT - 2)

    return snake, direction, food_x, food_y

def draw_board(snake, food_x, food_y):
    clear_screen()
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) in snake:
                if (x, y) == snake[0]:
                    print(SNAKE_HEAD, end='')
                else:
                    print(SNAKE_BODY, end='')
            elif x == food_x and y == food_y:
                print(FOOD, end='')
            else:
                print(' ', end='')
        print()

def move_snake(snake, direction):
    head_x, head_y = snake[0]
    if direction == UP:
        new_head = (head_x, head_y - 1)
    elif direction == DOWN:
        new_head = (head_x, head_y + 1)
    elif direction == LEFT:
        new_head = (head_x - 1, head_y)
    elif direction == RIGHT:
        new_head = (head_x + 1, head_y)
    snake.insert(0, new_head)
    snake.pop()

def check_collision(snake, food_x, food_y):
    head = snake[0]
    if head[0] == food_x and head[1] == food_y:
        snake.append((food_x, food_y))
        return True
    return False

def check_game_over(snake):
    head = snake[0]
    if (
        head[0] <= 0 or head[0] >= WIDTH - 1 or
        head[1] <= 0 or head[1] >= HEIGHT - 1 or
        head in snake[1:]
    ):
        return True
    return False

def play_game():
    snake, direction, food_x, food_y = initialize_game()

    while True:
        draw_board(snake, food_x, food_y)

        key = get_key()
        if key in (UP, DOWN, LEFT, RIGHT):
            direction = key

        move_snake(snake, direction)

        if check_collision(snake, food_x, food_y):
            food_x = random.randint(1, WIDTH - 2)
            food_y = random.randint(1, HEIGHT - 2)

        if check_game_over(snake):
            break

    draw_board(snake, food_x, food_y)
    print("Game over!")

# Start the game
play_game()
