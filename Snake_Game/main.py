from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
# Create the Screen.

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(n=0)

game_is_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
lose = False
while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()


    if snake.head.distance(food) <= 15:
        food.refresh()
        scoreboard.add()
        snake.extend()

    y_position = snake.head.ycor()
    x_position = snake.head.xcor()

    if  x_position > 280 or x_position < -280 or y_position < -280 or y_position > 280:
        game_is_on = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False



print("Whoops! You're out.")
scoreboard.game_over()







screen.exitonclick()
