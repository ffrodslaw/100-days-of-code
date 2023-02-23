from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager():

    def __init__(self):
        self.cars = []
        self.speed =  STARTING_MOVE_DISTANCE

    def create_car(self):

        random_y = random.randint(-240, 250)
        car = Turtle("square")
        car.penup()
        car.color(random.choice(COLORS))
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.goto(310, random_y)
        self.cars.append(car)

    def move_cars(self):

        for car in self.cars:
            new_x = car.xcor() - self.speed
            car.goto(new_x, car.ycor())

    def speed_up(self):

        self.speed += MOVE_INCREMENT
        for car in self.cars:
            new_x = car.xcor() - self.speed
            car.goto(new_x, car.ycor())


