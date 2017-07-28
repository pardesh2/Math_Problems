#! usr/bin/env python3
'''
drawing the nth stage of the sierpinski arrowhead curve
'''

import turtle
import math

def main():
    while True:
        stage = int(input('Enter the stage: '))
        turtle.clearscreen()
        if stage == -1:
            break
        turtle.bgcolor('black')
        turtle.color('purple')
        turtle.hideturtle()
        turtle.speed(0)

        edge_length = 500/2**stage

        turtle.pu()
        turtle.goto(-250, 250 * math.sqrt(3) * -1/3)
        turtle.pd()

        moves_list = turn_generator(stage)

        if stage % 2 == 1:
            turtle.setheading(60)
        
        draw_arrowhead(edge_length, moves_list)
        turtle.forward(edge_length)


def turn_generator(stage):
    '''
    Generating a list of either 60 or 360 degree turns
    :param stage: the stage of the curve that will be drawn
    '''
    initial = []
    if stage == 0:
        intial = [60, 60]
    elif stage > 0:
        initial = turn_generator(stage - 1)
        flipped = [360 - i for i in initial]
        initial = flipped + [60] + initial + [60] + flipped 
    return initial

def draw_arrowhead(edge_length, turn_sequence):
    '''
    Going through the list of moves and moving the turtle accordingly to draw the figure
    :param edge_length: the distance of each forward move
    :param turn_sequence: the list of turns to draw the figure
    '''
    for i in turn_sequence:
        turtle.forward(edge_length)
        if i > 180:
            turtle.left(360 - i)
        elif i < 180:
            turtle.right(i)

main()
