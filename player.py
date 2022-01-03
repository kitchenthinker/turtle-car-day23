import turtle

GAP_BETWEEN_CELLS = 20
STEPS = 10


class PlayerTurtle(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
        self.penup()

    def set_default_position(self, xcor=0, ycor=0):
        self.setposition(xcor, ycor)

    def go_north(self):
        self.forward(STEPS)



