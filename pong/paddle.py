from turtle import Turtle

PADDLE_STEPS = 35

class Paddle(Turtle) :

    def __init__(self, position) :
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=4, stretch_len=0.6)
        self.color("white")
        self.penup()
        self.goto(position)

    def move_up(self) :
        new_y = self.ycor() + PADDLE_STEPS   
        self.goto(self.xcor(), new_y)

    def move_down(self) :
        new_y = self.ycor() - PADDLE_STEPS
        self.goto(self.xcor(), new_y)