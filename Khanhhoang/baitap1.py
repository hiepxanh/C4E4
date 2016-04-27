from turtle import *
shape("turtle")
for s in range(7,2,-1):
    if(s%2==1):
        color("black","yellow")
    elif(s%2==0):
        color("green","red")
    begin_fill()
    for i in range(s):
        forward(100)
        left(360/s)
    end_fill()
