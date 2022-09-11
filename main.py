from turtle import Screen
import time

from scoreboard import Scoreboard
from snake import Snek
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snek()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.leftwards, "Left")
screen.onkey(snake.rightwards, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    score.keep_score()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.clear()
        score.num_eaten += 1

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # Detect collision with tail
    # if head collides with any segment of tail:
    for segment in snake.snek_bod[1:]:
        if snake.head.distance(segment) < 10:
            # trigger game over
            game_is_on = False
            score.game_over()

screen.exitonclick()
