## bar chart
from turtle import *
shape("turtle")
def draw_bar(x, z):
    penup()
    goto(x,0)
    pendown()
    color("red")
    begin_fill()
    
    for i in range(2):
        forward(int(20))
        left(90)
        forward(int(z))
        left(90)    
    end_fill()

def draw_bar_chart():
    x=5
    zs = [50, 200, 150, 70, 25, 125]
    for z in zs:
        draw_bar(x,z)
        x = x + 30
draw_bar_chart()

## salary

file = open("ss5_data.txt")
def luong(): 
    for line in file:
        l = line.split()
        salary = int(l[1]) * int(l[2])   
        print(str.format("After {0} hours, {1} receives total {2} $", l[1], l[0], salary))
luong()




