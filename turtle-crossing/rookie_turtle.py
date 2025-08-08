from turtle import Turtle

MOVE_STEPS = 20

class RookieTurtle(Turtle) :
    def __init__(self) :
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.color("green")
        self.penup()
        self.reposition()

        
    def reposition(self) :    
        self.goto(0,-270)
        
    def move_up(self) :
        new_y = self.ycor() + MOVE_STEPS
        self.goto(self.xcor(), new_y)