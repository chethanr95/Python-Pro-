from turtle import Screen
from snake import Snake
from food import Food
from scorecard import Scorecard
import time


#create the screen
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")

#turn off screen - turtle movement trace - animations
screen.tracer(0)

#create the snake
snake = Snake()

#create the food
food = Food()

#create the scorecard
score = Scorecard()

#game on off control 
game_on = True

#main 
#game run logic

screen.listen()

while game_on :
    #update screen, used along with screen.tracer()  
    screen.update()

    time.sleep(0.15)
    
    screen.onkey(key = "Up", fun = snake.move_up)
    screen.onkey(key = "Down", fun = snake.move_down)
    screen.onkey(key = "Left", fun = snake.move_left)
    screen.onkey(key = "Right", fun = snake.move_right)

    snake.move()

    #detect collission with wall
    if snake.wall_hit() :
        score.game_over()
        game_on = False

    #detect collission with food
    if food.food_eaten(snake.head) :
        score.increment_points()
        snake.grow(food.pencolor())
        
    #detect collission with snake body
    if snake.body_hit() :
        score.game_over()
        game_on = False


screen.exitonclick()