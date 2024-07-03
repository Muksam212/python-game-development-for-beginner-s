from random import choice, random
from turtle import *
from base import vector

def value():
    #[-5, 3] - [3, 5]
    return (3 + random() * 2) * choice([1, -1])

ball = vector(0, 0) #position at the center
aim = vector(value(), value()) #speed randomly to the ball

state = {1: 0, 2:0} #for both the player

def move(player, change):
    state[player] += change

def rectangle(x, y, width, height):
    up()
    goto(x, y) #go to that position
    down()
    begin_fill()
    for count in range(2):
        forward(width)
        left(90) #two side of rectangle should be 90
        forward(height)
        left(90)

    end_fill()


def draw():
    clear()
    rectangle(-200, state[1], 10, 50) #player 1
    rectangle(190, state[2], 10, 50) #Player 2

    ball.move(aim)
    x = ball.x
    y = ball.y

    dot(10)
    update()
    #if the movement inside the boundary ot not
    if y < -200 or y > 200:
        aim.y = -aim.y
    if x < -185:
        low = state[1]
        high = state[1] + 50
        if low <= y <= high:
            aim.x = -aim.x
        else:
            return 
        
    if x > 185:
        low = state[2]
        high= state[2] + 50
        if low <= y <= high:
            aim.x = -aim.x
        else:
            return 
        
    ontimer(draw, 50)
    
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: move(1, 20), 'w')
onkey(lambda: move(1, -20), 's')
onkey(lambda: move(2, 20), 'i')
onkey(lambda: move(2, 20), 'k')
draw()
done()