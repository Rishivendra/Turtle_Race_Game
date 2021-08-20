from turtle import Turtle, Screen

import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)  # sets the width and height of the main window
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter color:")  # Pop up a dialog window for input of a string
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    new_turtle.color(colours[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False  # stop race
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have Won! The {winning_color} is the turtle winner!")
            else:
                print(f"You have Lost! The {winning_color} is the turtle winner!")
        rand_distance = random.randint(0, 10)
        turtle.fd(rand_distance)

screen.exitonclick()
