from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.level = 0
        self.write(f"Level : {self.level}", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level : {self.level}", font=FONT)
