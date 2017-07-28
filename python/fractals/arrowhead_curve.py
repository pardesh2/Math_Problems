#! usr/bin/env python3
'''
drawing the nth stage of the sierpinski arrowhead curve
'''

import turtle
import math

turtle.bgcolor('black')
turtle.color('purple')
turtle.hideturtle()
turtle.speed(0)

stage = int(input('Enter the stage: '))
edge_length = 500/2**stage

def turn(stage):
    '''
    generating a list containing the degree measures of each turn
    :param stage: the stage of the curve to be drawn 
    '''
    initial = [60, 60]
    if stage > 0:
        for i in range(stage - 1):
            flipped = [360 - i for i in initial]
            initial = flipped + [60] + initial + [60] + flipped
        arrowhead(edge_length, initial)

def arrowhead(edge_length, turn_sequence):
    '''
    reading each element in the list generated above and actually moving the turle
    :param turn_sequence: the list that contains the turn measures
    :param edge_length: the distance of each side in the nth stage
    '''
    for i in turn_sequence:
        turtle.forward(edge_length)
        if i > 180:
            turtle.left(360 - i)
        elif i < 180:
            turtle.right(i)

turtle.pu()
turtle.goto(-250, 250 * math.sqrt(3) * -1/3)
turtle.pd()

if stage % 2 == 1:
    turtle.setheading(60)

turn(stage)
turtle.forward(edge_length)

turtle.exitonclick()
