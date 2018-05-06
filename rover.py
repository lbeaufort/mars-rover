import logging

from direction import Direction, North, East, South, West
from position import Position


class Rover:
    def __init__(self, position=Position(0, 0), direction=Direction.N):
        self.position = position
        self.direction = direction

    def get_position(self):
        return self.position

    def get_direction(self):
        return self.direction

    def change_direction(self, command):

        if command == "R":
            self.direction = self.direction.turn_right()
        else:
            self.direction = self.direction.turn_left()

    def move_position(self, command):

        if command == "F":
            self.move_forward()
        else:
            self.move_backward()

    def move_forward(self):

        if self.direction == North():
            self.position.y += 1
        elif self.direction == East():
            self.position.x += 1
        elif self.direction == South():
            self.position.y -= 1
        elif self.direction == West():
            self.position.x -= 1
        else:
            print('Invalid direction')

    def move_backward(self):

        if self.direction == North():
            self.position.y -= 1
        elif self.direction == East():
            self.position.x -= 1
        elif self.direction == South():
            self.position.y += 1
        elif self.direction == West():
            self.position.x += 1
        else:
            print('Invalid direction')

    def execute(self, commands):

        for command in commands:
            if command.upper() in ("F", "B"):
                self.move_position(command.upper())
            elif command.upper() in ("L", "R"):
                self.change_direction(command.upper())
            else:
                print('Invalid command')
