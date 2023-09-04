from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
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

screen.exitonclick()
