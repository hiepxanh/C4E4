from turtle import *
speed(0)

penup()
backward(200)
pendown()

# From Session 1:
for x in range (7,2,-1):
    begin_fill()
    
    for i in range(x):
        forward(100)
        left(360/x)
        if x%2==1:
            color("red","blue")
        else:
            color("black","yellow")
                
    end_fill()

penup()
forward(200)
pendown()

# Exercise 1: Square
color("green","yellow")
begin_fill()
for x in range (4):
    forward (100)
    left (90)
end_fill()

penup()
forward(200)
pendown()

# Exercise 2: Triangle
color("green","yellow")
begin_fill()
for x in range (3):
    forward (100)
    left (120)
end_fill()

penup()
right(90)
forward(200)
pendown()

# Exercise 3: Circle
color("green","yellow")
begin_fill()
circle(50)
end_fill()

penup()
right (90)
forward(200)
pendown()

# Exercise 4: Multi-circle
color("green", "white")
begin_fill()
for x in range (40):
    circle(50)
    left(9)
end_fill()

penup()
forward(200)
pendown()




