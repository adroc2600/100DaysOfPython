from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__ (self, length=3, size=1, shape="square", color="white", speed=10):
        self.snake_list = []
        self.length = length
        self.size = size
        self.step = 20 * self.size 
        self.shape = shape
        self.color = color
        self.speed = speed
        self.create_snake(self.length)
        self.head = self.snake_list[0]

    def create_snake(self, length):
        x = 0
        y = 0

        for _ in range(length):
            t = Turtle(self.shape)
            t.penup()
            t.resizemode("user")
            t.shapesize(stretch_wid=self.size, stretch_len=self.size)
            t.color(self.color)
            t.speed(self.speed)
            t.goto(x, y)

            self.snake_list.append(t)
            x -= self.step

    def grow(self):
        tail = self.snake_list[-1]

        t = Turtle(self.shape)
        t.penup()
        t.resizemode("user")
        t.shapesize(stretch_wid=self.size, stretch_len=self.size)
        t.color(self.color)
        t.speed(self.speed)
        t.goto(tail.xcor(), tail.ycor())

        self.snake_list.append(t)

    def move(self):
        for segment in range(len(self.snake_list)-1, 0, -1):
            self.snake_list[segment].goto(self.snake_list[segment-1].xcor(),self.snake_list[segment-1].ycor())
        
        self.head.forward(self.step)

    def up(self):
        if self.head.heading() == UP or self.head.heading() == DOWN:
            return
        else:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() == UP or self.head.heading() == DOWN:
            return
        else:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() == LEFT or self.head.heading() == RIGHT:
            return
        else:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() == LEFT or self.head.heading() == RIGHT:
            return
        else:
            self.head.setheading(RIGHT)