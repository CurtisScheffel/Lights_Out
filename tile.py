class Tile:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def flip_tile(self):
        if self.value == 0:
            self.value = 1
        else:
            self.value = 0

    def get_value(self):
        return self.value
