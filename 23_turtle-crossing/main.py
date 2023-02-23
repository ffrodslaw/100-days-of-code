import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.onkeypress(player.move, "Up")

game_is_on = True
loop = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()

    # create new cars
    if loop % 6 == 0:
        car_manager.create_car()

    # detect collision with car:
    for car in car_manager.cars:
        if player.distance(car) < 20 and player.ycor() != -280:
            game_is_on = False
            scoreboard.game_over()

    # detect turtle reached top of screen
    if player.ycor() > 300:
        scoreboard.level_up()
        car_manager.speed_up()
        player.reset()

    loop += 1

screen.exitonclick()
