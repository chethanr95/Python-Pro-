from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")

class Scorecard :

    def __init__(self) :

        self.points = 0
        self.score = Turtle()
        self.score.hideturtle()
        self.score.penup()
        self.score.goto(0,270)
        self.score.color("white")

        #self.write_score(score)
        self.write_score()


    #def write_score(self, score) :  
    def write_score(self) :  
        self.score.clear()
        self.score.write(arg=f"Score: {self.points}", align=ALIGNMENT, font=FONT)

    def game_over(self) :
        end_card = Turtle()
        end_card.hideturtle()
        end_card.penup()
        end_card.color("white")
        end_card.goto(0,0)
        end_card.write(arg=f"GAME OVER !", align=ALIGNMENT, font=FONT)

    def increment_points(self) :
        self.points += 1
        self.write_score()