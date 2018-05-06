from flask import Flask

from rover import Rover
from position import Position
from direction import Direction

app = Flask(__name__)


@app.route('/')
def hello_world():
    direction = Direction.W
    position = Position(0, 0)
    mars_rover = Rover(position, direction)
    return 'Mars rover is at position {0} and facing {1}.'.format(
        mars_rover.position, mars_rover.direction)
