from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

is_game_on = True
while is_game_on:
    screen.update()
    ball.move()
    time.sleep(0.1)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if (ball.distance(r_paddle) < 60 and ball.xcor() > 320) or (ball.distance(l_paddle) < 60 and ball.xcor() < -320):
        ball.bounce_x()
    if ball.xcor() > 390 or ball.xcor() < -390:
        is_game_on = False
        print("Game over")

screen.exitonclick()
