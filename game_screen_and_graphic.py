import turtle
from turtle import Turtle, TurtleScreen, _Screen

PEN_SIZE = 10
DRAWING_SPEED = 0
DEFAULT_OBJECTS_COLOUR = 'black'
DEFAULT_SCREEN_COLOUR = 'white'
DEFAULT_ALIGNMENT = 50
DEFAULT_SCREEN_WIDTH = 600
DEFAULT_SCREEN_HEIGHT = 600
DEFAULT_SCOREBOARD_FONT = ("Small fonts", 20, "bold")


class GameScreen(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.screen = turtle.Screen()
        self.screen.clear()
        self.screen.title("TURTLE CROSSING THE ROAD")
        self.screen.setup(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.screen.bgcolor(DEFAULT_SCREEN_COLOUR)
        self.screen.tracer(0)
        self.screen.update()
        self.scoreboard = ScoreBoard(DEFAULT_SCREEN_WIDTH/2, DEFAULT_SCREEN_HEIGHT/2)
        self.scoreboard.write_scoreboard()

    def update_graphic(self):
        self.scoreboard.write_scoreboard()


class ScoreBoard:

    def __init__(self, v_screen_width, v_screen_height):
        self.player_score = LevelObject(v_screen_width, v_screen_height)
        self.screen_width = v_screen_width
        self.screen_height = v_screen_height

    def write_scoreboard(self):
        self.player_score.write_score()

    def write_game_over(self):
        game_over = turtle.Turtle()
        game_over.write("GAME OVER!", False, align="center", font=DEFAULT_SCOREBOARD_FONT)

class LevelObject(Turtle):

    def __init__(self, v_screen_width, v_screen_height):
        super().__init__()
        self.color("blue")
        self.speed(DRAWING_SPEED)
        self.pensize(PEN_SIZE)
        self.penup()
        self.hideturtle()
        self.level = 1
        self.screen_width = v_screen_width
        self.screen_height = v_screen_height

    def write_score(self):
        self.clear()
        self.setposition(-self.screen_width/2 - DEFAULT_ALIGNMENT, self.screen_height - DEFAULT_ALIGNMENT)
        self.write(f"LEVEL: {self.level}", False, align="center", font=DEFAULT_SCOREBOARD_FONT)

    def increase_level(self):
        self.level += 1
