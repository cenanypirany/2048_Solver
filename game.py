from game_class import Game

controls = {
    'w': 'up',
    's': 'down',
    'a': 'left',
    'd': 'right'
}

game = Game()
game.start()
game.print_board()

while True:
    move = input("Enter move: ")

    if move in controls:
        game.make_move(controls[move])
        game.print_board()
    elif move == 'q':
        exit()
    else:
        game.print_board()
        print(f"Please enter the keys: {controls}. Or 'q' to quit.")