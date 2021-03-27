import numpy as np
import os

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

grid = np.random.choice((0,2,4,8), size=(4,4))
print(grid)
