import numpy as np
import random
import os

class Game():
    def __init__(self):
        self.grid = np.zeros((4,4), dtype=int)
        self.turn_count = 0

    def start(self):
        self.grid[self.get_open_coord()] = self.get_rand_2_4()
        self.grid[self.get_open_coord()] = self.get_rand_2_4()

    def print_board(self):
        os.system('clear')
        print(f"Turns: {self.turn_count}")
        grid = str(self.return_grid())
        grid = grid.replace('[','|').replace(']','|').replace('0',' ')
        grid = ' ' + grid[1:-1]
        print(grid)

    def game_over(self):
        self.print_board()
        print(f"Game Over! Your highest tile is: {np.max(self.grid)}")
        exit()

    def get_rand_2_4(self):
        return random.choices((2,4), weights=(0.9, 0.1))[0]

    def get_open_coord(self):
        if 0 in self.grid:
            arr = np.where(self.grid == 0)
            open_pos = [(x, y) for x, y in zip(arr[0], arr[1])]
            return(random.choice(open_pos))
        else:
            self.game_over()

    def return_grid(self):
        return(self.grid)

    def make_move(self, direction):
        grid = np.copy(self.grid)
        
        if direction == 'down':
            for i in range(4):
                grid[:, i] = np.flip(self.push_line(np.flip(grid[:, i])))
        elif direction == 'up':
            for i in range(4):
                grid[:, i] = self.push_line(grid[:, i])
        elif direction == 'right':
            for i in range(4):
                grid[i, :] = np.flip(self.push_line(np.flip(grid[i, :])))   
        elif direction == 'left':
            for i in range(4):
                grid[i, :] = self.push_line(grid[i, :])

        if False not in np.equal(grid, self.grid):    
            if 0 not in self.grid:
                self.game_over()
            else:
                self.return_grid()
        else:
            self.grid = grid
            self.end_turn()
    
    def return_count(self):
        return self.turn_count

    def end_turn(self):
        self.turn_count += 1
        self.grid[self.get_open_coord()] = self.get_rand_2_4()
        self.return_grid()

    def push_line(self, line):
        line = self.strip_zeros(line)
        for i in range(3):
            val_1 = line[i]
            val_2 = line[i + 1]
            if val_1 == val_2:
                line[i] = val_1 * 2
                line[i + 1] = 0    
        return self.strip_zeros(line)

    def strip_zeros(self, line):
        line = line[line != 0]
        zeros = 4 - len(line)
        for _ in range(zeros):
            line = np.append(line, 0)
        return line