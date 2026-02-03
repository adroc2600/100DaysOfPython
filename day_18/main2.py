from turtle import Turtle, Screen


my_turtle = Turtle()
my_screen = Screen()

for _ in range(15):
    # my_turtle.pencolor("black")
    # my_turtle.forward(10)
    # my_turtle.pencolor("white")
    # my_turtle.forward(10)

    #Mo Betta
    my_turtle.forward(10)
    my_turtle.teleport(abs(my_turtle.pos())+10)

my_screen.exitonclick()