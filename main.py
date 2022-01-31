from turtle import Screen
from paddle_1 import PaddleLeft
from paddle_2 import PaddleRight
from ball import Ball
from scoreboard import Scoreboard
import time

# init
screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
paddle_1 = PaddleLeft()
paddle_2 = PaddleRight()
ball = Ball()
scoreboard = Scoreboard()

#bind key to functions
screen.listen()
screen.onkey(paddle_1.up, "w")
screen.onkey(paddle_1.down, "s")
screen.onkey(paddle_2.up, "Up")
screen.onkey(paddle_2.down, "Down")

game_is_on =  True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddles
    if ball.distance(paddle_1) < 40 and ball.xcor() < -320 or ball.distance(paddle_2) < 40 and ball.xcor() > 320:
        ball.bounce_x()

    #detect right
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #detect left
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()