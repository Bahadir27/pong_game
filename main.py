import time
from turtle import Turtle, Screen
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle

INITIAL_POSITION = 350

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


paddle_right = Paddle(position=(INITIAL_POSITION, 0))
paddle_left = Paddle(position=(-INITIAL_POSITION, 0))
ball = Ball()
scoreboard = Scoreboard()


# screen listens the keystrokes
screen.listen()
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")
refresh_rate = 0.1

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # pass

    # detect collision with vertical walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # print(ball.distance(paddle_left))
    # detect collision with paddles
    if ball.xcor() > 340 and ball.distance(paddle_right) < 50 or ball.xcor() < -340 and ball.distance(paddle_left) < 50:
        ball.bounce_x()

    # detect if ball os out of the game right side
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect if ball os out of the game left side
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()

