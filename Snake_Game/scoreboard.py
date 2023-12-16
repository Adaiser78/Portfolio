from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.collision_count = 0
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score: {self.collision_count}", align=ALIGNMENT, font=FONT)



    def add(self):
        self.collision_count += 1
        self.clear()
        self.write(f"Score: {self.collision_count}", align='center', font=('Arial', 20, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align='center', font=('Arial', 20, 'normal'))