from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,x ,y , height=1, width=5):
        super().__init__()
        self.speed(10)
        self.shape("square")
        self.goto(x, y)
        self.penup()
        self.setheading(90)
        self.turtlesize(height,width)
        self.color("white")
        

    def move_up(self):
        self.forward(20)
    
    def move_down(self):
        self.backward(20)
    
