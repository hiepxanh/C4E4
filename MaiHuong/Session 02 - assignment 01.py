from turtle import *
speed(0)

for s in range (6,2,-1):
    begin_fill()
    for i in range(s):
        
        forward(100)
        left(360/s)
        if s%2 == 1:
            color("black", "green")
        else:
            color("red", "yellow")
    end_fill()


penup()
forward(300)
pendown()

color("pink", "blue")
t = 20
begin_fill()
for i in range(20):
    circle(50)
    left(360/t)
end_fill()
