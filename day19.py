# Day 19: higher order functions and event listeners
##################
import random
import turtle
import turtle as t

timmy = t.Turtle()
screen = t.Screen()


# def move_forwards():
#     timmy.forward(10)
#
# # screen.listen()
# # screen.onkey(key="space", fun=move_forwards)
# # screen.exitonclick()
#
# ##################
#
# # etch a sketch
#
# # add more functions
#
#
# def move_left():
#     timmy.setheading(timmy.heading() + 10)
#
#
# def move_right():
#     timmy.setheading(timmy.heading() - 10)
#
#
# def move_backwards():
#     timmy.backward(10)
#
#
# def clear_screen():
#     timmy.reset()
#
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="a", fun=move_left)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="d", fun=move_right)
# screen.onkey(key="c", fun=clear_screen)
#
# screen.exitonclick()

########################

# Turtle race

is_race_on = False
screen.setup(width=500, height=400)
# popup
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for i in range(0,6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + i * 40)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost. The {winning_color} turtle is the winner!")
            is_race_on = False
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()
