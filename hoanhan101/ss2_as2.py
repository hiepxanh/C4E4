from turtle import *

speed(0)

color("green","yellow")

penup()
backward(300)
pendown()

for d in range(4,2,-1):
    begin_fill()
    for x in range(d):
        forward(50)
        left(360/d)
    end_fill()

penup()
forward(200)
pendown()

for x in range(6):
    circle(50)
    left(60)

penup()
forward(300)
pendown()


for x in range(36):
    circle(50)
    left(10)

