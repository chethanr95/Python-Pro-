from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")

class Score(Turtle) :
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()    
        #Note turtle is a single turtle, but it writes in two diffeent locations
        self.l_score = 0
        self.r_score = 0
        self.color("silver")
        self.update_score()

    def update_score(self) :
        self.clear()
        self.goto(0,250)
        self.write("| SCORE |", align = ALIGNMENT, font = FONT )
        self.goto(-100,250)
        self.write(self.l_score, align = ALIGNMENT, font = FONT)
        self.goto(100, 250)
        self.write(self.r_score, align = ALIGNMENT, font = FONT)

    def point_to_left_paddle(self) :    
        self.l_score += 1
        self.update_score()

    def point_to_right_paddle(self) :
        self.r_score += 1
        self.update_score()    