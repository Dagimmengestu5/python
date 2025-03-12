########################## Turtle race ######################################
from turtle import Turtle, Screen
import random
new_turtle = Turtle()

screen = Screen()

screen.setup(width=500, height=400)
user_guess = screen.textinput(title="make a name", prompt="Enter which color of turtle Win: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

all_turtles = []
for tuttle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[tuttle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[tuttle_index])
    all_turtles.append(new_turtle)

if user_guess:
    race_activity = True


while race_activity:


    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_activity = False
            winning_color = turtle.pencolor()
            if winning_color == user_guess:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)





screen.exitonclick()
################ keyboard key move
#
# def move_forward():
#     d.forward(10)
# def move_backward():
#     d.backward(10)
# def turn_left():
#   new_heading = d.heading() + 10
#   d.setheading(new_heading)
# def turn_right():
#   new_heading = d.heading() - 10
#   d.setheading(new_heading)
# def clear():
#     d.clear()
#     d.penup()
#     d.home()
#     d.pendown()
#
# screen.listen()
# screen.onkey(move_forward, "w")
# screen.onkey(move_backward, "s")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")
# screen.onkey(clear, "c")
# screen.exitonclick()