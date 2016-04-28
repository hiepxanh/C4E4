from turtle import *
color("pink","yellow")

for s in range (6,2,-1):
    if s % 2 == 1:
        color("blue","red")
    
    else:
        color("purple","green")
    begin_fill()
    for i in range (s):
      forward (100)
      left (360/s)
    end_fill ()
