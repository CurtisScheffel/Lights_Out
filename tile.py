class Tile:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return str(self.color)

    def __repr__(self):
        return str(self.color)

    def flip_tile(self):
        if self.color == 0:
            self.color = 1
        else:
            self.color = 0

