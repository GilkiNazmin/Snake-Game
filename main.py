from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import ScoreBoard
import time
from constants import snake_const


screen = Screen()
is_game_on = True
screen.setup(snake_const.SCREEN_SETUP[0], snake_const.SCREEN_SETUP[1])
screen.title(snake_const.SCREEN_TITLE)
screen.bgcolor(snake_const.BACKGROUND_COLOR)
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()

screen.onkey(snake.move_up, key="Up")
screen.onkey(snake.move_down, key="Down")
screen.onkey(snake.move_left, key="Left")
screen.onkey(snake.move_right, key="Right")
while is_game_on:
    screen.update()
    time.sleep(snake_const.SCREEN_UPDATE_DELAY)
    snake.move_snake_forward()

    # Detect collision with the food
    if snake.head.distance(food) < snake_const.HEAD_FOOD_COLLISION_DISTANCE:
        food.refresh()
        snake.extend_body()
        scoreboard.increase_score()

    # Detect collision with the wall
    snake_xcor = snake.head.xcor()
    snake_ycor = snake.head.ycor()
    if ((snake_xcor > snake_const.WALL_COORDINATE[0]) or (snake_xcor < snake_const.WALL_COORDINATE[1]) or
            (snake_ycor > snake_const.WALL_COORDINATE[0]) or (snake_ycor < snake_const.WALL_COORDINATE[1])):
        is_game_on = False
        # scoreboard.compare_highscore()
        scoreboard.game_over()

    # Detect collision with the tail
    for snake_body_part in snake.snake_body[1:]:
        if snake.head.distance(snake_body_part) < snake_const.BODY_COLLISION_DISTANCE:
            is_game_on = False
            scoreboard.compare_highscore()
            scoreboard.game_over()

screen.exitonclick()
