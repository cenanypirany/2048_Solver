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

def redraw_grid(grid):
    grid[rand_free_coord()] = rand_2_4()
    grid[rand_free_coord()] = rand_2_4()
    os.system('clear')
    return grid

def strip_zeros(line):
    line = line[line != 0]
    zeros = 4 - len(line)
    for _ in range(zeros):
        line = np.append(line, 0)
    return line

def press_line(line):
    line = strip_zeros(line)
    for i in range(3):
        val_1 = line[i]
        val_2 = line[i + 1]
        if val_1 == val_2:
            line[i] = val_1 * 2
            line[i + 1] = 0    
    return strip_zeros(line)

def make_move(grid, direction):
    if direction == 'down':
        for i in range(4):
            grid[:, i] = np.flip(press_line(np.flip(grid[:, i])))
    elif direction == 'up':
        for i in range(4):
            grid[:, i] = press_line(grid[:, i])
    elif direction == 'right':
        for i in range(4):
            grid[i, :] = np.flip(press_line(np.flip(grid[i, :])))   
    elif direction == 'left':
        for i in range(4):
            grid[i, :] = press_line(grid[i, :])
    
    return(grid)

#Game Loop
keys = {
    'i': 'up',
    'k': 'down',
    'j': 'left',
    'l': 'right'
}

grid = np.zeros((4,4), dtype=int)
print(redraw_grid(grid))
move = ''

while True:
    move = input()

    if move in keys:
        grid = make_move(grid, keys[move])

        print(redraw_grid(grid))
    elif move == 'q':
        exit()
    else:
        print(f"Please enter the keys: {keys}. Or 'q' to quit.")