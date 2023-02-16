Day 16: object oriented paradigm (OOP)

import turtle

timmy = turtle.Turtle()  # create turtle object from the turtle module
print(timmy)
timmy.shape("turtle")
timmy.color("cyan4")
timmy.forward(100)

my_screen = turtle.Screen()
print(my_screen.canvheight) # attribute of object

my_screen.exitonclick() # method is a function associated with object

##################

from prettytable import PrettyTable

table = PrettyTable()
print(table)

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", " Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)

# Project: OOP Coffee machine, see oop-coffee-machine folder

