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
        with open("high_score.txt", mode='r') as file:
            self.clear()
            self.high_score = int(file.read())
            self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT,font=(FONT, FONT_SIZE, FONT_TYPE))

    def update_score(self):
        self.score += 1
        self.clear()
        if self.score > self.high_score:
            with open("high_score.txt", mode='w') as file:
                file.write(str(self.score))
                self.high_score = self.score
                self.clear()
                self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT,font=(FONT, FONT_SIZE, FONT_TYPE))
        else:
            self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT,font=(FONT, FONT_SIZE, FONT_TYPE))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT,font=(FONT, FONT_SIZE, FONT_TYPE))

