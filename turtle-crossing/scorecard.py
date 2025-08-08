from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 10, "normal")

class Levelcard(Turtle) :
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(0, 270)

        self.level = 1
        
        self.write_level()

    def write_level(self) :
        self.clear()
        self.write(f"Level: {self.level}", align = ALIGNMENT, font = FONT )

    def level_up(self) :
        self.level += 1
        self.write_level()

    def game_over(self) :    
        self.write_level()
        self.goto(0,0)
        self.write("Game Over !", align = ALIGNMENT, font = FONT )