#! usr/bin/env python3
"""
drawing the nth stage of sierpinski's triangle
"""

import turtle
import math

turtle.bgcolor('black')
turtle.speed(0)
turtle.hideturtle()
turtle.color('lime green')

stage = int(input('Enter the stage: '))

def triangle(edge_length):
    for i in range(3):
        turtle.forward(edge_length)
        turtle.left(120)

def position(edge_length):
    turtle.pu()
    turtle.goto(-edge_length, -edge_length/4 * math.sqrt(3))
    turtle.pd()
    if stage == 0:
        triangle(2 * edge_length)
    elif stage > 0: 
        sierpinski(stage, edge_length)
        turtle.pu()
        turtle.goto(0, -edge_length/4 * math.sqrt(3))
        turtle.pd()
        sierpinski(stage, edge_length)
        turtle.pu()
        turtle.goto(-edge_length/2, math.sqrt(3) * edge_length/4)
        turtle.pd()
        sierpinski(stage, edge_length)

def sierpinski(stage, edge_length):
    if stage - 1 == 0:
        triangle(edge_length)
    elif stage - 1 > 0:
        (initial_x, initial_y) = turtle.position()
        for i in range(3):
            if i == 1:
                turtle.pu()
                turtle.goto(initial_x + edge_length/2, initial_y)
                turtle.pd()
            elif i == 2:
                turtle.pu()
                turtle.goto(initial_x + edge_length/4, initial_y + edge_length/4 * math.sqrt(3))
                turtle.pd()
            sierpinski(stage - 1, edge_length/2)

position(500/2)

turtle.exitonclick()
