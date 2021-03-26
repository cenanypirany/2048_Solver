# Starting up
import numpy as np
import random

grid = np.zeros((4,4), dtype=int)

print(grid)

def rand_free_coord():
    while True:
        x = random.randint(0,3)
        y = random.randint(0,3)
        if grid[x, y] == 0:
            return (x, y)

def rand_2_4_weighted():
    return random.choices(population=[2,4], weights=[0.9, 0.1])

grid[rand_free_coord()] = rand_2_4_weighted()[0]
grid[rand_free_coord()] = rand_2_4_weighted()[0]

print(grid)