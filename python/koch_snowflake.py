#! usr/bin/env python3
"""
drawing the nth stage of the koch curve
"""

import turtle
import math

turtle.bgcolor('black')
turtle.speed(0)
turtle.hideturtle()
turtle.color('sky blue')

stage = int(input('Enter the stage: '))

turtle.penup()
turtle.goto(-250, -250/3 * math.sqrt(3)) 
turtle.pendown()

def koch_basic(edge_length, moves_list):
    """
    reading all of the moves and executing them

    :param edge_length: the edge length of the nth stage
    :param moves_list: the list that contains all of the moves
    """
    n = 0
    for move in moves_list:
        if move == 'forward':
            turtle.forward(edge_length)
        elif move == 'right':
           turtle.right(60)
        elif move == 'left':
           turtle.left(120)

def moves_list(stage):
    """
    generating the complete list of moves
    :param stage: the stage of the koch curve to be drawn
    """
    L = ['forward', 'right', 'forward', 'left', 'forward', 'right', 'forward']
    if stage == 0:
        turtle.forward(500)
    elif stage > 0:
        for i in range(stage - 1):
            length = len(L)
            L = L * 4
            L.insert(length, 'right')
            L.insert(length*2 + 1, 'left')
            L.insert(length*3 + 2, 'right')
        koch_basic(500/(3**(stage)), L)

for i in range(3):
   moves_list(stage)
   turtle.left(120)

turtle.exitonclick()
