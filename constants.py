class Constants:
    def __init__(self):
        self.WALL_COORDINATE = [290, -290]
        self.SCREEN_SETUP = (600, 600)
        self.BACKGROUND_COLOR = "black"
        self.SCREEN_UPDATE_DELAY = 0.2
        self.HEAD_FOOD_COLLISION_DISTANCE = 15
        self.BODY_COLLISION_DISTANCE = 10
        self.SCREEN_TITLE = "Nazmin's Snake Game"
        self.STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
        self.MOVING_DISTANCE = 15
        self.UP = 90
        self.DOWN = 270
        self.LEFT = 180
        self.RIGHT = 0
        self.SNAKE_SHAPE = "square"
        self.SNAKE_COLOR = "red"
        self.SNAKE_WIDTH = 0.9
        self.SNAKE_LENGTH = 0.8
        self.FOOD_X_Y_POS = (-230, 230)
        self.FOOD_SHAPE = "circle"
        self.FOOD_COLOR = "yellow"
        self.FOOD_SPEED = "fastest"
        self.FOOD_WIDTH = 0.5
        self.FOOD_LENGTH = 0.5
        self.SCOREBOARD_COLOR = "white"
        self.ALIGNMENT = "center"
        self.FONT = ('Arial', 18, 'normal')
        self.GAME_OVER_ALIGNMENT = (0, 0)
        self.SCOREBOARD_POSITION = (0, 260)
        self.FILENAME = "highscore.txt"


snake_const = Constants()
