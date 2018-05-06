class Direction:
    """
      N
    W   E
      S
    """
    def __eq__(self, other):

        if isinstance(other, Direction):
            return type(self) == type(other)
        else:
            return False

    def __repr__(self):
        return type(self).__name__


class North(Direction):
    """
      W <- N -> E
    """

    def turn_left(self):
        return West()

    def turn_right(self):
        return East()


class East(Direction):
    """
      N <- E -> S
    """
  #  print(self.__name__)

    def turn_left(self):
        return North()

    def turn_right(self):
        return South()


class South(Direction):
    """
      E <- S -> W
    """
    def turn_left(self):
        return East()

    def turn_right(self):
        return West()


class West(Direction):
    """
      N <- W -> S
    """
    def turn_left(self):
        return South()

    def turn_right(self):
        return North()

Direction.N = North()
Direction.E = East()
Direction.S = South()
Direction.W = West()
