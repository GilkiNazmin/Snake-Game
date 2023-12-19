from turtle import Turtle
from constants import snake_const


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color(snake_const.SCOREBOARD_COLOR)
        self.score = 0
        self.highscore = 0
        self.penup()
        self.goto(snake_const.SCOREBOARD_POSITION[0], snake_const.SCOREBOARD_POSITION[1])
        self.hideturtle()
        self.set_highscore()
        self.update_score_board()

    def update_score_board(self):
        self.write(f"Score = {self.score}, Highscore = {self.highscore}", align=snake_const.ALIGNMENT,
                   font=snake_const.FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score_board()

    def game_over(self):
        self.goto(snake_const.GAME_OVER_ALIGNMENT)
        self.write("GAME OVER", align=snake_const.ALIGNMENT, font=snake_const.FONT)

    def set_highscore(self):
        with open(snake_const.FILENAME) as file:
            highscore = file.readline()
            self.highscore = int(highscore)

    def compare_highscore(self):
        if self.highscore < self.score:
            with open(snake_const.FILENAME, "w") as file:
                file.write(str(self.score))
            file.close()
