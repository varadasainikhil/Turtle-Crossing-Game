import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()

player = Player()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")
new_car = CarManager()
count = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if count % 6 == 0:
        new_car.add_car()
        new_car.move_car()
    if player.ycor() > 270:
        player.reset_position()
        scoreboard.increase_level()
    x = new_car.return_car_list()
    for car in x:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
    count += 1

screen.exitonclick()
