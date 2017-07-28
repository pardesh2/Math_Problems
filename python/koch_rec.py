import turtle
import math

stage = int(input('Enter the stage: '))

turtle.bgcolor('black')
turtle.color('sky blue')
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(-250, -250/3 * math.sqrt(3)) 
turtle.pendown()

def koch(edge_length, stage):
    if stage == 0:
        turtle.forward(edge_length)
    elif stage > 0:
        for i in [60, -120, 60, 0]:
            koch(edge_length/3, stage - 1)
            turtle.right(i)

for i in range(3):
    koch(500, stage)
    turtle.left(120)

turtle.exitonclick()
