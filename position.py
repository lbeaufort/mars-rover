class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):

        if isinstance(other, Position):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __repr__(self):
        return '({0},{1})'.format(self.x, self.y)
