#! usr/bin/env python3

import turtle
import math

def main():
    stage = int(input('Enter the stage: '))
    angle = int(input('Enter the angle: '))

    turtle.bgcolor('black')
    turtle.hideturtle()
    turtle.color('lime green')
    turtle.speed(0)

    stage_length = 500/3**stage
    move_to_start(stage, angle, stage_length)
    L = create_list(stage, angle)
    for i in range(3):
        draw_koch(stage_length, L, angle)
        turtle.left(120)

    turtle.exitonclick()

def move_to_start(stage, angle, stage_length):
    theta = math.radians(angle)
    side_length = stage_length
    for i in range(stage):
        side_length = 2*side_length*(1 + math.sin(theta/2))

    half_side_length = side_length/2
    median = half_side_length * math.sqrt(3)
    turtle.pu()
    turtle.goto(-1 * half_side_length, median * -1/3)
    turtle.pd()

def draw_koch(edge_length, moves_list, angle):
    n = 0
    for move in moves_list:
        if move == 'forward':
            turtle.forward(edge_length)
        elif move == 'right':
           turtle.right(90 - angle/2)
        elif move == 'left':
           turtle.left(180 - angle)

def create_list(stage, angle):
    L = ['forward']
    if stage == 0:
        return L
    for i in range(stage):
        L = L + ['right'] + L + ['left'] + L + ['right'] + L
    return L

main()
