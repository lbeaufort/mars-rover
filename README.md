# Mars Rover Challenge

Inspired by [@mfreyre](https://github.com/mfreyre/mars-rover-python)'s object-oriented programming workshop at [Codeland 2018](http://codelandconf.com/). This is a work in progress - feel free to enter an issue or PR!

## Local development
Set up a virtual environment - I use [pyenv](https://github.com/pyenv/pyenv-virtualenv)

Install Flask: `pip install Flask`

## Challenge

You are on a team programming the remotely controlled Mars Rover robot.
Given an initial starting point (x,y), an initial direction the robot is facing, and a list of commands, you want to be able to calculate what the end point (x’, y’) will be.
The robot can move forward and backward, as well as turn left and right. Turning does not change the position of the rover, but the action must update the cardinal direction of the rover.

Using the test file as guidance, please develop a program that will calculate the final location of the rover after it has executed a list of commands.

### Available commands
"L" -> turn left

"R" -> turn right

"F" -> go forward

"B" -> go backward

### Cardinal Directions
East

North

West

South

## To Execute tests

Run `python tests.py`
