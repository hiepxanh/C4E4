<<<<<<< HEAD
from turtle import*
speed(0)
color("black","yellow")
begin_fill()
for x in range(4):
    forward(100)
    left(90)
end_fill()

penup()
forward(200)
pendown()
side=3
begin_fill()
for x in range(3):
    forward(100)
    left(360/side)
end_fill()
right(90)

penup()
forward(200)
pendown()
begin_fill()
circle(50)
end_fill()
right(90)

penup()
forward(200)
pendown()
color("green","white")
begin_fill()
for x in range (50):
    circle(50)
    left(10)
end_fill()
penup()
left(180)
forward(300)
pendown()
right(135)

for s in range(7,2,-1):
    if(s%2==1):
        color("black","yellow")
    elif(s%2==0):
        color("black","brown")
    begin_fill()
    for i in range(s):
        forward(100)
        left(360/s)
    end_fill()
=======
from turtle import*
speed(0)
color("black","yellow")
begin_fill()
for x in range(4):
    forward(100)
    left(90)
end_fill()

penup()
forward(200)
pendown()
side=3
begin_fill()
for x in range(3):
    forward(100)
    left(360/side)
end_fill()
right(90)

penup()
forward(200)
pendown()
begin_fill()
circle(50)
end_fill()
right(90)

penup()
forward(200)
pendown()
color("green","white")
begin_fill()
for x in range (50):
    circle(50)
    left(10)
end_fill()
penup()
left(180)
forward(300)
pendown()
right(135)

for s in range(7,2,-1):
    if(s%2==1):
        color("black","yellow")
    elif(s%2==0):
        color("black","brown")
    begin_fill()
    for i in range(s):
        forward(100)
        left(360/s)
    end_fill()
>>>>>>> 1e55ec78a1dd02332e11163893373d4bb1e86aed
