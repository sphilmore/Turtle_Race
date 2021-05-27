from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title= "Make you bet!", prompt= "Which turtle do you think will win the race? Enter a color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50,88]
x_position = -230
turtle_list = []

for things in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[things])
    new_turtle.goto(x=x_position, y=y_position[things])
    turtle_list.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The winning color is the {winning_color} turtle")
            else:
                print(f"You lost! The winning color is the {winning_color} turtle")


        distance = random.randint(0, 10)
        turtle.forward(distance)



screen.exitonclick()