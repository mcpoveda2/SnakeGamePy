from turtle import Screen
from  Snake import Snake
from  food import Food
import time

#Screen Setuo
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game by Michael Poveda")
screen.tracer(0)


snake = Snake()
food = Food()

screen.listen()
screen.onkey(fun = snake.up, key="Up")
screen.onkey(fun = snake.down, key="Down")
screen.onkey(fun = snake.left, key="Left")
screen.onkey(fun = snake.right, key="Right")


#Inicio del juego
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collisions with the food

    if(snake.head.distance(food)<15):
        print("me choque jeje")
        food.refresh()

screen.exitonclick()