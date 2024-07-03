from turtle import *

state = {"turn":0}

def spinner():
    #draw fidget spinner using turtle
    clear()
    angle = state['turn'] / 10

    right(angle)
    forward(100)

    dot(120, 'red')
    back(100)
    right(120)
    forward(100)

    dot(120, 'green')
    back(100)
    right(120)
    forward(100)

    dot(120, 'blue')
    back(100)
    right(120)
    update()

def animate():
    if state['turn'] > 0:
        state['turn'] -= 1
    spinner()
    ontimer(animate, 20)

def flick():
    #for flick of fidget
    state['turn'] += 10 #increase every time with 10 units

setup(420, 420, 370, 0)
hideturtle()
tracer(False) #there won't be any delay
width(20)
onkey(flick,'space')
listen() #listen to the user connection
animate()
done()