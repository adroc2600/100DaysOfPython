from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    
    def __init__(self, start_x, start_y, height=2):
        super().__init__()
        self.color(random.choice(COLORS[0:]))
        self.penup()
        self.setheading(180)
        self.shape("square")
        self.turtlesize(stretch_len=height)
        self.setpos(start_x, start_y)

    def move(self, amount=MOVE_INCREMENT):
        self.forward(amount)
