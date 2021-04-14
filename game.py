from game_class import Game
from algo_class import Sequence
import sys
import random
import pandas as pd

## Human controls
controls = {
    'w': 'up',
    's': 'down',
    'a': 'left',
    'd': 'right'
}

if len(sys.argv) > 1:
    mode = 'api'
    algo = Sequence(sys.argv[1])
else:
    mode = 'human'

game = Game(mode,100)
game.start()
if mode == 'human':
    game.print_board()

while game.loop():
    if game.mode == 'human':
        move = input("Enter move: ")
        if move in controls:
            game.make_move(controls[move])
            game.print_board()
        elif move == 'q':
            game.game_over()
        else:
            game.print_board()
            print(f"Please enter the keys: {controls}. Or 'q' to quit.")

    elif game.mode == 'api':
        move = algo.get_move()
        game.make_move(move)

if mode == 'api':
    print('Sequence:')
    print(algo.sequence)
    df = pd.DataFrame(game.return_stats())
    df.to_csv('stats.csv', index=False)
    