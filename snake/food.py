from turtle import Turtle
import random

COLORS = ("blue", "red", "green", "yellow", "pink", "orange", "purple")
X_BORDER = 260
Y_BORDER = 260

class Food(Turtle) :

    def __init__(self) :
        super().__init__()

        self.shape("circle")
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.penup()
        self.create_food()

    def create_food(self) :    
        self.color(random.choice(COLORS))
        x = random.randint(-X_BORDER, X_BORDER)
        y = random.randint(-X_BORDER, X_BORDER)
        self.goto(x,y)

    def food_eaten(self, snake_head) :
        if snake_head.distance(self) < 15 :
            self.clear()
            self.create_food()
            
            return True
        else :
            return False
