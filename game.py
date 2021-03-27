# Starting up
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
    os.system('cls')
    print(grid)

#Game Loop
keys = ('i','k','j','l')
up = keys[0]
down = keys[1]
left = keys[2]
right = keys[3]

grid = np.zeros((4,4), dtype=int)
move = ''
while True:
    redraw_grid()

    if move == up:
        pass
    elif move == down:
        pass
    elif move == left:
        pass
    elif move == right:
        pass
    elif move == 'q':
        exit()
    else:
        print(f"Please enter the keys: {keys}")