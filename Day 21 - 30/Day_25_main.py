################# American cuntry gussing game

import turtle
import pandas

screen = turtle.Screen()
screen.title("Game")
image = "files/blank_states_img.gif"
screen.addshape(image)
# turtle = turtle.Turtle()
turtle.shape(image)
# def get_mouse_color(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_color)
# turtle.mainloop()
data = pandas.read_csv("files/50_states.csv")

all_state = data.state.to_list()
guessed_state = []


while len(guessed_state) < 50:

    answer_state = screen.textinput ( title=F"{len ( guessed_state )}/50 States Correct" ,
                                      prompt="Guess the state" ).title()
    missing_state = [state for state in all_state if state not in guessed_state]
    new_data = pandas.DataFrame(missing_state)
    new_data.to_csv("state_to.csv")
    if answer_state in all_state and answer_state not in guessed_state :
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state ]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state )
    if answer_state == "Exit":
        break


