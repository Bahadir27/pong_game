from turtle import Turtle, Screen
from paddle import Paddle

INITIAL_POSITION = 350

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
# screen.tracer(0)


paddle_left = Paddle(position=(INITIAL_POSITION, 0))
paddle_right = Paddle(position=(-INITIAL_POSITION, 0))

# screen listens the keystrokes
screen.listen()
screen.onkey(paddle_left.go_up, "Up")
screen.onkey(paddle_left.go_down, "Down")
screen.onkey(paddle_right.go_up, "w")
screen.onkey(paddle_right.go_down, "s")

game_is_on = False
while game_is_on:
    # screen.update()
    pass

screen.exitonclick()

