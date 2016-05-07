from turtle import*
def draw_bar(x,v,y,c):
    begin_fill()
    penup()
    goto(x,0)
    pendown()
    for i in range(2):
        color(c,c)
        forward(v)
        left(90)
        forward(y)
        left(90)
    end_fill()
l=[50,200,150,70,25,125]
x=10
for y in l:
    draw_bar(x,15,y,'red')
    x=x+25
    penup()
    goto(x,0)
    pendown()
    
