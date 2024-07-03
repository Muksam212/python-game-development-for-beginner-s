from turtle import *
from random import randrange
from base import square, vector

#variable
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(-10, 0)

def inside(head):
    #check if the head is inside the boundary or not
    return -200 < head.x < 190 and -200 <head.y < 190

def change(x, y):
    #aim to change the direction of snake
    aim.x = x
    aim.y = y

def move():
    #move snake one segment forward
    head = snake[-1].copy()
    head.move(aim)
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return
    snake.append(head)

    #checking the condition if snake eats food
    if head == food:
        print("Snake: ", len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()
    for body in snake:
        square(body.x, body.y, 9, 'black')
    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen() #Listen to the connection
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10),'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()