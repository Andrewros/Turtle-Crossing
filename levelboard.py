from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.level = 1

    def writescore(self):
        self.goto(x=-250, y=230)
        self.write("Level : " + str(self.level), False,
                   font=("courier", 18, "normal"))

    def game_over(self):
        self.home()
        self.write("GAME OVER", False,
                   font=("courier", 24, "normal"), align="center")
