###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle as t
import random

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

# print(rgb_colors)

###################

# 10 x 10 spots
# dots: 20 radius, 50 space

timmy = t.Turtle()
timmy.hideturtle()
t.colormode(255)
position = 0

for _ in range(10):

    for _ in range(10):
        timmy.pendown()
        timmy.color(random.choice(rgb_colors))
        timmy.dot(20)
        timmy.penup()
        timmy.forward(50)

    position +=50
    timmy.goto(0, timmy.heading() + position)

screen = t.Screen()
screen.exitonclick()