from direction import Direction
from position import Position


class Rover:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def get_position(self):
        return self.position

    def get_direction(self):
        return self.direction

    def turn_right(self):

        if self.direction == "N":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "S"
        elif self.direction == "S":
            self.direction = "W"
        else:
            self.direction = "N"

    def turn_left(self):
        if self.direction == "N":
            self.direction = "W"
        elif self.direction == "E":
            self.direction = "N"
        elif self.direction == "S":
            self.direction = "E"
        else:
            self.direction = "S"

    def change_direction(self, command):

        if command == "R":
            self.turn_right()
        else:
            self.turn_left()

    def move_position(self, command):

        if command == "F":
            self.move_forward()
        else:
            self.move_backward()

    def move_forward(self):

        if self.direction == "N":
            self.position.y += 1
        elif self.direction == "E":
            self.position.x += 1
        elif self.direction == "S":
            self.position.y -= 1
        else:
            self.position.x -= 1

    def move_backward(self):

        if self.direction == "N":
            self.position.y -= 1
        elif self.direction == "E":
            self.position.x -= 1
        elif self.direction == "S":
            self.position.y += 1
        else:
            self.position.x += 1

    def execute(self, commands):

        for command in commands:
            if command.upper() in ("F", "B"):
                self.move_position(command.upper())
            elif command.upper() in ("L", "R"):
                self.change_direction(command.upper())
            else:
                print('Invalid command')
