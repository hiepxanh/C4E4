from turtle import *
for s in range(7,2,-1):
    if s%2 == 0:
        color("green","yellow")
    else:
        color("blue","pink")
    begin_fill()
    for i in range(s):
        forward(100)
        left(360/s)
    end_fill()
