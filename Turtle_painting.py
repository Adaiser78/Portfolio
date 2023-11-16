import turtle
import random
turtle.colormode(255)
tim = turtle.Turtle()
tim.penup()
tim.hideturtle()


color_list = [(229, 228, 227), (226, 224, 225), (198, 175, 119), (125, 36, 23), (187, 157, 50), (170, 104, 56), (5, 56, 83),
(201, 216, 205), (109, 67, 85), (39, 35, 34), (223, 224, 227), (84, 141, 61), (20, 122, 175), (111, 161, 176),
(75, 38, 48), (8, 67, 47), (65, 154, 134), (132, 41, 43), (184, 98, 81), (183, 180, 181), (210, 200, 108),
(178, 201, 186), (150, 180, 170), (90, 143, 158), (28, 81, 59), (193, 190, 192), (17, 78, 98), (215, 184, 172),
(190, 190, 195), (78, 72, 31)]

tim.speed(20)
right = False
x = False
for _ in range(10):
    if right:
        tim.left(90)
        tim.forward(20)
        tim.left(90)
        x = True
    elif x:
        tim.right(90)
        tim.forward(20)
        tim.right(90)
    for _ in range(11):
        color = (random.choice(color_list))
        tim.dot(20, color)
        tim.forward(20)
    tim.dot(20, random.choice(color_list))

    right = not right









#TODO: I don't fucking know how to do it. You're supposed to make the turtle draw
#TODO: 10 rows and 10 columns of random dots that are each 20 in size and spaced by 50.


screen = turtle.Screen()
screen.exitonclick()
