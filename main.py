from board import *
import numpy as np

board = Board(5, 5)

if __name__ == '__main__':
    # game_won = False
    #
    # while not game_won:
    #     board.print_board()
    #     print("Select a tile to flip.")
    #     print('Row index:')
    #     row = int(input())
    #     print('Column index:')
    #     column = int(input())
    #     board.flip_tile(row, column)

    array1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
    array2 = np.array([[9,8,7],[6,5,4,],[3,2,1]])

    arrayProduct = np.matmul(array1,array2)

    print(arrayProduct)

