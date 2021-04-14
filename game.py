from game_class import Game
from algo_class import Sequence

## Human controls
controls = {
    'w': 'up',
    's': 'down',
    'a': 'left',
    'd': 'right'
}

## Algorithm
algo = Sequence(['right','up','left','down'])

mode = 'api'
game = Game(mode,20)
game.start()
if mode == 'human':
    game.print_board()

while True:
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
    