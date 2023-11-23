from turtle import Turtle, Screen
import random

# Create all the turtles and create a list.

tim = Turtle(shape="turtle")
tommy = Turtle(shape="turtle")
jack = Turtle(shape="turtle")
alan = Turtle(shape="turtle")
ray = Turtle(shape="turtle")
george = Turtle(shape="turtle")
turtles = [tim, tommy, jack, alan, ray, george]

# Set up the screen, its size. Ask for input.

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet!", "Which turtle will win the race? Enter a Color:")

# Create a colors list.

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
''' 
Set y_coordinate = -40. Iterate through the turtles and colors to assign each one a different color.
Move each turtle to the same x coordinate and the current y coordinate. Increase the y_coordinate in each
iteration. 

'''

y_coordinate = -60
for index in range(6):
    turtle = turtles[index]
    turtle.color(colors[index])
    turtle.penup()
    turtle.goto(x=-230, y=y_coordinate)
    y_coordinate += 30

if user_bet:
    race_is_on = True
else:
    race_is_on = False

while race_is_on:
    for turtle in turtles:
        turtle.forward(random.randint(1, 10))
        current_x = int(turtle.xcor())
        if current_x >= 230:
            race_is_on = False
            winner_color = turtle.color()[0]


if winner_color == user_bet:
    print("Your bet was right. Good job!")
else:
    print("Your bet was wrong. Good luck next time!")
screen.exitonclick()
