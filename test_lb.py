from rover import Rover

my_rover = Rover()

#my_rover.turn_right()

print(my_rover.get_direction())
#my_rover.change_direction("R")

# my_rover.change_direction("L")

my_rover.execute("R")

print(my_rover.get_direction())

print(my_rover.get_position())

print(my_rover.get_direction())

my_rover.execute(("F", "F"))
print(my_rover.get_position())
