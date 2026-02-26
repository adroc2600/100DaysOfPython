import turtle
import pandas

my_screen = turtle.Screen()
my_image = turtle.Turtle()
image = "blank_states_img.gif"
my_screen.addshape(image)

my_image.shape(image)

answer_state = my_screen.textinput(title="US STATES", prompt="Enter a US State:")

my_states = pandas.read_csv("50_states.csv")

correct_guesses = []
while len(correct_guesses) <= 50:
    exists = my_states[my_states.state == answer_state.capitalize()]
    if exists.empty:
        print("WRONG")
    else:
        if correct_guesses.count(exists.state.item()) >= 1:
            pass
        else:
            text = turtle.Turtle()
            text.hideturtle()
            text.penup()
            #text.teleport(x=exists['x'].iloc[0], y=exists['y'].iloc[0])
            text.teleport(x=exists.x.item(), y=exists.y.item())
            #text.write(exists['state'].iloc[0])
            text.write(exists.state.item())
            correct_guesses.append(exists.state.item())
    answer_state = my_screen.textinput(title=f"US STATES {len(correct_guesses)}/50", prompt="Enter a US State:")


my_screen.exitonclick()

