from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.updating_scoreboard()
        self.hideturtle()

    def updating_scoreboard(self):
        self.write(f"Player 1 Score:{self.score_1} | Player 2 Score: {self.score_2}", align="center", font=('Arial', 20, 'normal'))


