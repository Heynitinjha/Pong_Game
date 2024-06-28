import time
from turtle import Turtle, Screen
from peddle import Peddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("Black")
screen.setup(width=800, height=600)
screen.title("Pong Game")

screen.tracer(0)

peddle = Turtle()
r_peddle = Peddle((350, 0))
l_peddle = Peddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_peddle.go_up, "Up")
screen.onkey(r_peddle.go_down, "Down")

screen.onkey(l_peddle.go_up, "w")
screen.onkey(l_peddle.go_down, "s")

is_on = True
while is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_peddle) < 50 and ball.xcor() > 320 or ball.distance(l_peddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()




screen.exitonclick()
