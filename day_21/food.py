from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=.5,stretch_len=.5)
        self.color("blue")
        self.move()

    def move(self):
        rand_x = random.randint(-260, 260)
        rand_y = random.randint(-260, 260)
        self.goto(rand_x, rand_y)