import time
from turtle import Turtle, Screen

from ball import Ball
from paddle import Paddle

INITIAL_POSITION = 350

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


paddle_left = Paddle(position=(INITIAL_POSITION, 0))
paddle_right = Paddle(position=(-INITIAL_POSITION, 0))
ball = Ball()

# screen listens the keystrokes
screen.listen()
screen.onkey(paddle_left.go_up, "Up")
screen.onkey(paddle_left.go_down, "Down")
screen.onkey(paddle_right.go_up, "w")
screen.onkey(paddle_right.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # pass

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
        pass

screen.exitonclick()

