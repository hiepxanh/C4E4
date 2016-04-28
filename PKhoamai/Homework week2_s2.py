from turtle import *
speed(0)
color("green", "yellow")
s=4
    
begin_fill()
for x in range(s):
    forward(100)
    left(360/s)
        
penup()
s=3
setx(105)
sety(105)
  
pendown()

for x in range(s):
    forward(100)
    left(360/s)
   
penup()
setx(-105)
sety(-105)

pendown()
circle(100)
end_fill()

penup()
setx(270)
sety(-120)
pendown()
for x in range (100):
    circle(100)
    left(8)


