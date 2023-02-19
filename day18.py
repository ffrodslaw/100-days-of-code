# Day 18: More graphics with turtle
##################################

import turtle as t
timmy = t.Turtle()

timmy.shape("turtle")
# timmy.color("red")

# Challenge 1: draw sqaure

# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)
#
# screen = t.Screen()
# screen.exitonclick()

# Challenge 2: Draw a dashed line

# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()
#
# screen = t.Screen()
# screen.exitonclick()

# Challenge 3: Drawing different shapes

import random
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# timmy.forward(100)
#
# for i in range(3, 10):
#     angle = 360 / i
#
#     for _ in range(i):
#         timmy.right(angle)
#         timmy.forward(100)
#
#     timmy.color(random.choice(colors))
#
#
# screen = t.Screen()
# screen.exitonclick()

# Challenge 4: Random walk

timmy.pensize(10)
timmy.speed(10)

angles = [0, 90, 180, 270]

# for _ in range(100):
#     timmy.right(random.choice(angles))
#     timmy.forward(20)
#     timmy.color(random.choice(colors))
#
#
# screen = t.Screen()
# screen.exitonclick()


# Challenge 5: Random RGB colors

# t.colormode(255) # change colormode to rgb
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
# for _ in range(100):
#     timmy.right(random.choice(angles))
#     timmy.forward(20)
#     timmy.color(random_color())
#
#
# screen = t.Screen()
# screen.exitonclick()

# Challenge 6: Spirograph

timmy.pensize(1)
timmy.speed(15)

for _ in range(36): # 360 degrees / 10 degrees is gap
    timmy.color(random.choice(colors))
    timmy.circle(100)
    timmy.right(10)
    timmy.circle(100)



screen = t.Screen()
screen.exitonclick()