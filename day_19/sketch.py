from turtle import Turtle, Screen

def controls(t,s):

    def move_forward():
        t.forward(1)
    def move_backward():
        t.backward(1)
    def turn_left():
        t.left(1)
    def turn_right():
        t.right(1)
    def clear():
        t.clear()
        t.teleport(0,0)
        

    s.onkey(fun=move_forward, key="w")
    s.onkey(fun=move_backward, key="s")
    s.onkey(fun=turn_left, key="a")
    s.onkey(fun=turn_right, key="d")
    s.onkey(fun=clear, key="c")

my_turtle = Turtle()
my_screen = Screen()
my_screen.listen()
my_turtle.speed(10)

controls(my_turtle, my_screen)

my_screen.exitonclick()