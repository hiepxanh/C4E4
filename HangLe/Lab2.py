#Wave1:
from turtle import*
side=input("Which shape do you want to draw, triangle, square or pentagon?, (input number of side=)))")
for x in range(int(side)):
    forward(100)
    left(360/int(side))
    

#Wave2:
from turtle import*
def arrow(n):
    for x in range(n):
        forward(x)
        penup()
        forward(n/5)
        pendown()

arrow(50)

#Wave3:
from turtle import *
def hexagon():
    for x in range(6):
        forward(100)
        left(60)

for x in range(10):
    hexagon()
    forward(100)
    right(60)
        
#Wave4:
import turtle
def forward(distance):
    while distance > 0:
        if turtle.distance(0,0) > 100:
            angle = turtle.towards(0,0)
            turtle.setheading(angle)
        turtle.forward(1)
        distance = distance - 1

forward(110)

Wave5:
import turtle
def draw_spiral(radius):
    speed = 1
    while True:
        turtle.forward(speed)
        turtle.left(10)
        speed += 0.1
        if turtle.distance(turtle.xcor(), turtle.ycor()) > radius:
            break
draw_spiral(100)

control
from turtle import *
def di_thang():
    forward(45)
def lui_lai():
    back(45)
def quay_phai():
    right(45)
def quay_trai():
    left(45)
onkey(di_thang,"Up")
onkey(lui_lai,"Down")
onkey(quay_phai,"Right")
onkey(quay_trai,"Left")
listen()

