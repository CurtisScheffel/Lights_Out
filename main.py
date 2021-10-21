from board import *

board = Board(5, 5)

if __name__ == '__main__':
    game_won = False

    while not game_won:
        board.print_board()
        print("Select a tile to flip.")
        print('Row index:')
        row = int(input())
        print('Column index:')
        column = int(input())
        board.flip_tile(row, column)


