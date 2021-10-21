from tile import *


class Board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.board = [[0 for x in range(height)] for y in range(width)]
        for h in range(height):
            for w in range(width):
                tile = Tile(0)
                self.board[h][w] = tile

    def print_board(self):
        for h in range(self.height):
            print(self.board[h])

    def get_adjacent_tiles(self, row, column):
        # Returns orthogonally adjacent tiles to [row,column].
        # Will return 2 to 4 tiles depending on the location.
        height_index = self.height - 1
        width_index = self.width - 1
        if row == 0:
            if column == 0:
                # Top Left Corner - Returns 2 Tiles
                return [0, 1], \
                       [1, 0]
            elif column == width_index:
                # Top Right Corner - Returns 2 Tiles
                return [0, width_index - 1], \
                       [1, width_index]
            else:
                # Top Row - Returns 3 Tiles
                return [0, column - 1], \
                       [0, column + 1], \
                       [1, column]
        elif row == height_index:
            if column == 0:
                # Bottom Left Corner - Returns 2 Tiles
                return [height_index - 1, 0], \
                       [height_index, 1]
            elif column == width_index:
                # Bottom Right Corner - Returns 2 Tiles
                return [height_index - 1, width_index], \
                       [height_index, width_index - 1]
            else:
                # Bottom Row - Returns 3 Tiles
                return [height_index - 1, column], \
                       [height_index, column - 1], \
                       [height_index, column + 1]
        else:
            if column == 0:
                # Leftmost Column - Returns 3 Tiles
                return [row + 1, 0], \
                       [row - 1, 0], \
                       [row, 1]
            elif column == width_index:
                # Rightmost Column - Returns 3 Tiles
                return [row + 1, width_index], \
                       [row - 1, width_index], \
                       [row, width_index - 1]
            else:
                # Middle of the board - Returns 4 Tiles
                return [row + 1, column], \
                       [row - 1, column], \
                       [row, column + 1], \
                       [row, column - 1]

    def flip_tile(self, row, column):
        tiles_to_flip = self.get_adjacent_tiles(row, column)
        for tile in tiles_to_flip:
            self.board[tile[0]][tile[1]].flip_tile()
        self.board[row][column].flip_tile()

