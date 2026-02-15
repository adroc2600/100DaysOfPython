from turtle import Turtle

ALIGNMENT= "center"
FONT = "Arial"
FONT_SIZE = 16
FONT_TYPE = "normal"

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.clear()
        self.write(f"{self.left_score} / {self.right_score}", align=ALIGNMENT,font=(FONT, FONT_SIZE, FONT_TYPE))
        
    def update_left_score(self):
        self.clear()
        self.left_score += 1
        self.write(f"{self.left_score} / {self.right_score}", align=ALIGNMENT,font=(FONT, FONT_SIZE, FONT_TYPE))
        
    def update_right_score(self):
        self.clear()
        self.right_score += 1
        self.write(f"{self.left_score} / {self.right_score}", align=ALIGNMENT,font=(FONT, FONT_SIZE, FONT_TYPE))
        
