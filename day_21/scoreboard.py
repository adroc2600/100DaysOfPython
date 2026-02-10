from turtle import Turtle

ALIGNMENT= "center"
FONT = "Arial"
FONT_SIZE = 16
FONT_TYPE = "normal"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT,font=(FONT, FONT_SIZE, FONT_TYPE))
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT,font=(FONT, FONT_SIZE, FONT_TYPE))

