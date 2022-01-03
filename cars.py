from turtle import Turtle
import random
DEFAULT_ALIGNMENT = 5
DEFAULT_COLOURS = ['red', 'blue', 'yellow', 'green', 'purple', 'black']


class Car(Turtle):

    def __init__(self):
        super().__init__(visible=False)
        self.shape("square")
        self.color(random.choice(DEFAULT_COLOURS))
        self.shapesize(1, 2)
        self.pensize(10)
        self.penup()
        self.car_speed = random.randint(10, 20)
        self.setheading(180)

    def set_up_default_position(self, xcor=0, ycor=0):
        self.hideturtle()
        self.setposition(xcor, ycor)
        self.showturtle()

    def move(self):
        self.forward(self.car_speed)
