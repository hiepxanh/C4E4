from turtle import*
def draw_square (length,x):#x:color
    color(x)
    for i in range (4):
        forward(length)
        left(360/4)
draw_square(100,"blue")

for i in range(30):
    draw_square(i*5,'red')
    left(17)
    penup()
    forward(i*2)
    pendown()
