import numpy as np
import random
import os

#Functions
def rand_free_coord():
    if 0 not in grid:
        print("Game Over")
        print(f"Your largest tile was: { np.max(grid) }.")
        exit()
    else:
        free_array = np.where(grid == 0)
        free_postions = [(x, y) for x, y in zip(free_array[0], free_array[1])]
        return(random.choice(free_postions))

def rand_2_4():
    return random.choices((2,4), weights=(0.9, 0.1))[0]

def redraw_grid():
    grid[rand_free_coord()] = rand_2_4()
    grid[rand_free_coord()] = rand_2_4()
    os.system('clear')
    print(grid)

#Game Loop
keys = {
    'up': 'i',
    'down': 'k',
    'left': 'j',
    'right': 'l'
}

grid = np.zeros((4,4), dtype=int)
redraw_grid()
move = ''

while True:
    move = input()

    if move in keys.values():
        if move == keys['up']:
            pass
        elif move == keys['down']:
            pass
        elif move == keys['left']:
            pass
        elif move == keys['right']:
            pass

        redraw_grid()
    elif move == 'q':
        exit()
    else:
        print(f"Please enter the keys: {keys}. Or 'q' to quit.")