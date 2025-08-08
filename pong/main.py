from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

timer = 0.080

#setup the screen window
screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 550)
screen.title("|| PONG ||")
screen.tracer(0)

#create the paddle
r_paddle = Paddle((380,0))
l_paddle = Paddle((-380,0))

#create the ball, pong
ball = Ball()

#create scoreboard
score = Score()

screen.listen()

#main game logic
is_game_on = True

while is_game_on :
    screen.update()
    time.sleep(timer)

    #paddle movements upon key
    screen.onkey(key = "Up", fun = r_paddle.move_up)    
    screen.onkey(key = "Down", fun = r_paddle.move_down)
    screen.onkey(key = "w", fun = l_paddle.move_up)
    screen.onkey(key = "s", fun = l_paddle.move_down)

    #ball to be in motion always
    ball.keep_moving()

    #detect top & bottom wall hit, Bounce Y
    if ball.ycor() > 265 or ball.ycor() < -265 :
        print(ball.xcor(), ball.ycor())
        ball.bounce_y()
        
    #detect ball hit by the paddles  
    if ( ball.distance(r_paddle) <= 23 and ball.xcor() >= 360 ) or ( ball.distance(l_paddle) <= 23 and ball.xcor() >= -360) :
        ball.bounce_x()

    #detect ball missed the paddles and hit left or right side walls
    if ball.xcor() >= 380 :     
        #right paddle left the ball, point to left paddle

        score.point_to_left_paddle()
        ball.reset()
        #timer -= 0.02 
        
    if ball.xcor() <= -380 :
        #left paddle left the ball, point to right paddle

        score.point_to_right_paddle()
        ball.reset()
        #timer -= 0.001

#last line
screen.exitonclick()