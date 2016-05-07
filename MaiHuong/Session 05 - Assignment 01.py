from turtle import *
shape("turtle")
speed(0)

## turtle 1
##def draw_square(length, col):
##    color(col)
##    for i in range(4):
##            forward(length)
##            left(90)
##
##for i in range(30):
##    draw_square(i*5, 'red')
##    left(17)
##    penup()
##    forward(i*2)
##    pendown()
    


## turtle 2

def draw_star(x, y, length):
    for i in range(5):
        forward(length)
        left(144)
draw_star(0, 20, 100)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(0, 20, 100)



