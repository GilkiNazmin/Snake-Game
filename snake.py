from turtle import Turtle
from constants import snake_const


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake_body()
        self.head = self.snake_body[0]
        self.head.color("red")

    def create_snake_body(self):
        for position in snake_const.STARTING_POSITIONS:
            self.add_new_body_part(position)

    def add_new_body_part(self, position):
        new_snake_body = Turtle(snake_const.SNAKE_SHAPE)
        new_snake_body.color(snake_const.SNAKE_COLOR)
        new_snake_body.shapesize(snake_const.SNAKE_WIDTH, snake_const.SNAKE_LENGTH)
        new_snake_body.penup()
        new_snake_body.goto(position)
        self.snake_body.append(new_snake_body)

    def extend_body(self):
        self.add_new_body_part(self.snake_body[-1].position())

    def move_snake_forward(self):
        for snake in range(len(self.snake_body) - 1, 0, -1):
            x_pos = self.snake_body[snake - 1].xcor()
            y_pos = self.snake_body[snake - 1].ycor()
            self.snake_body[snake].goto(x_pos, y_pos)
        self.head.forward(snake_const.MOVING_DISTANCE)

    def move_up(self):
        if self.head.heading() != snake_const.DOWN:
            self.head.setheading(snake_const.UP)

    def move_down(self):
        if self.head.heading() != snake_const.UP:
            self.head.setheading(snake_const.DOWN)

    def move_left(self):
        if self.head.heading() != snake_const.RIGHT:
            self.head.setheading(snake_const.LEFT)

    def move_right(self):
        if self.head.heading() != snake_const.DOWN:
            self.head.setheading(snake_const.RIGHT)
