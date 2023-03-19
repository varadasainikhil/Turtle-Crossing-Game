from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars_list = []

    def add_car(self):
        turtle = Turtle("square")
        turtle.penup()
        turtle.color(random.choice(COLORS))
        x_position = 260
        y_position = random.randint(-230, 230)
        turtle.goto(x_position, y_position)
        turtle.shapesize(stretch_wid=1, stretch_len=2)
        self.cars_list.append(turtle)

    def move_car(self):
        for car in self.cars_list:
            car.backward(MOVE_INCREMENT*2)

    def return_car_list(self):
        return self.cars_list
