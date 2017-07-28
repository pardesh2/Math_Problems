import turtle

turtle.hideturtle()

stage = int(input('Enter the stage: '))

turtle.penup()
turtle.setx(-175)
turtle.pendown()

def triangle(edge_length):
    for i in range(1, 4):
        turtle.forward(edge_length)
        turtle.left(120)

def koch_basic(edge_length):
    n = 0
    for i in range(1, 8):
        solutions_list = ['forward', 'right', 'forward', 'left', 'forward', 'right', 'forward']
        move = solutions_list[n]
        if move == 'forward':
            turtle.forward(edge_length)
        elif move == 'right':
            turtle.right(60)
        else:
            turtle.left(120)        
        n = n + 1

def koch_1():
    n = 0
    d = 3
    L = ['a', 'right', 'a', 'left', 'a', 'right', 'a']
    for i in range(1, 7 + 1):
        move = L[n]
        if move == 'a':
            koch_basic(100/d)
        elif move == 'right':
            turtle.right(60)
        else:
            turtle.left(120)
        n = n + 1

def koch_2():
    n = 0
    d = 9

    L = ['a', 'right', 'a', 'left', 'a', 'right', 'a']
    list_length = len(L)
    L = L*4
    L.insert(list_length, 'right')
    L.insert(list_length * 2 + 1, 'left')
    L.insert(list_length * 3 + 2, 'right')

    for i in range(1, 4*7 + 3 + 1):
        move = L[n]
        if move == 'a':
            koch_basic(100/d)
        elif move == 'right':
            turtle.right(60)
        else:
            turtle.left(120)
        n = n + 1

def koch_3():
    n = 0
    d = 27
    counter = 0

    L = ['a', 'right', 'a', 'left', 'a', 'right', 'a']
    for i in range(1, 3):
        list_length = len(L)
        L = L * 4
        L.insert(list_length, 'right')
        L.insert(list_length * 2 + 1, 'left')
        L.insert(list_length * 3 + 2, 'right')

    for i in range(1, 7*4**(x-1)+15 + 1):
        move = L[n]
        if move == 'a':
            koch_basic(100/d)
            counter = counter + 1
        elif move == 'right':
            turtle.right(60)
        else:
            turtle.left(120)
        n = n + 1
        if counter == 4**x:
            n = 0
            counter = 0
            list_length = len(L)
            L = L*4
            L.insert(list_length, 'right')
            L.insert(list_length * 2 + 1, 'left')
            L.insert(list_length * 3 + 2, 'right')
    d = d*3

if stage == 0:
    triangle(300)
    turtle.exitonclick()
elif stage == 1:
    for i in range(1, 4):
        koch_basic(100)
        turtle.left(120)
    turtle.exitonclick()
else:
    for x in range(1, stage):
        if x == 1:
            for i in range(1, 4):
                koch_1()
                turtle.left(120)
        elif x == 2:
            for i in range(1, 4):
                koch_2()
                turtle.left(120)
        else:
            for i in range(1, 4):
                koch_3()
                turtle.left(120)
    turtle.exitonclick()
