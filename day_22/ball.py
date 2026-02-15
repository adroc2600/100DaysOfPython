from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.y_move = 10 * random.choice([1, -1])
        self.x_move = 10 * random.choice([1, -1])


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def hit_paddle(self):
        self.x_move *= -1

    def reset(self):
        self.home()
        self.y_move *= random.choice([1, -1])
        self.x_move *= random.choice([1, -1])
    
    def bounce(self):
        self.y_move *= -1
