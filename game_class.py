import numpy as np
import random
import os

class Game():

    def __init__(self):
        self.grid = np.zeros((4,4), dtype=int)
        self.turn_count = 0

    ##########################################################
    ## Key methods: start, print_board, end_turn, game_over ##
    ##########################################################

    def start(self):
        self.grid[self.get_open_coord()] = self.get_rand_2_4()
        self.grid[self.get_open_coord()] = self.get_rand_2_4()

    def print_board(self):
        os.system('clear')
        print(f"Turns: {self.turn_count}")
        grid = str(self.return_grid())
        grid = grid.replace('[','|').replace(']','|').replace('0',' ').replace('1 24','1024').replace('2 48','2048')
        grid = ' ' + grid[1:-1] + '\n'
        print(grid)

    def end_turn(self):
        self.turn_count += 1
        self.grid[self.get_open_coord()] = self.get_rand_2_4()
        self.return_grid()

    def game_over(self):
        self.print_board()
        print(f"Game Over! Your highest tile is: {np.max(self.grid)}")
        exit()

    ###############################################################################
    ## Helper functions: get_rand_2_4, return_count, get_open_coord, return_grid ##
    ###############################################################################

    def get_rand_2_4(self):
        return random.choices((2,4), weights=(0.9, 0.1))[0]

    def return_count(self):
        return self.turn_count

    def get_open_coord(self):
        if 0 in self.grid:
            arr = np.where(self.grid == 0)
            open_pos = [(x, y) for x, y in zip(arr[0], arr[1])]
            return(random.choice(open_pos))
        else:
            self.game_over()

    def return_grid(self):
        return(self.grid)

    #################################################
    ## Central move functions: can_move, make_move ##
    #################################################

    def can_move(self):        
        #check down
        grid = np.copy(self.grid)
        for i in range(4):
            grid[:, i] = np.flip(self.push_line(np.flip(grid[:, i])))

        if False in np.equal(grid, self.grid):
            return True

        #check up
        grid = np.copy(self.grid)
        for i in range(4):
            grid[:, i] = self.push_line(grid[:, i])

        if False in np.equal(grid, self.grid):
            return True

        #check right
        grid = np.copy(self.grid)
        for i in range(4):
            grid[i, :] = np.flip(self.push_line(np.flip(grid[i, :])))

        if False in np.equal(grid, self.grid):
            return True
 
        #check left
        grid = np.copy(self.grid)
        for i in range(4):
            grid[i, :] = self.push_line(grid[i, :])

        if False in np.equal(grid, self.grid):
            return True

        return False

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

        # Check to see if grid has changed after move, if so end turn
        if False in np.equal(grid, self.grid):    
            self.grid = grid
            self.end_turn()
        else:
            # If grid not changed after move, check all available move possibilities, if none then game over
            if not self.can_move(): 
                self.game_over()
            else:
                self.return_grid()    

    ######################################################
    ## Number summing functions: push_line, strip_zeros ##
    ######################################################

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
