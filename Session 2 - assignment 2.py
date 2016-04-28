from turtle import *
##draw filled polygon
speed(0)
color("green","yellow")
side = 3 #input 3 to draw a triangle, 4 to draw a square, 100 to draw a circle
begin_fill()
for x in range(side):
    forward(400/side)
    left(360/side)
end_fill()
##draw multiple circles
penup()
forward(400)
pendown()
color("green")
n = 20 #the number of circles
for x in range(n):
    circle(50)
    left(360/n)
