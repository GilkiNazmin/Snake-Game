from turtle import Turtle
import random
from constants import snake_const


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(snake_const.FOOD_SHAPE)
        self.penup()
        self.shapesize(stretch_wid=snake_const.FOOD_WIDTH, stretch_len=snake_const.FOOD_LENGTH)
        self.color(snake_const.FOOD_COLOR)
        self.speed(snake_const.FOOD_SPEED)
        self.refresh()

    def refresh(self):
        random_x = random.randint(snake_const.FOOD_X_Y_POS[0], snake_const.FOOD_X_Y_POS[1])
        random_y = random.randint(snake_const.FOOD_X_Y_POS[0], snake_const.FOOD_X_Y_POS[1])
        self.goto(random_x, random_y)
