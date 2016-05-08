from turtle import*
def draw_bar(x,y,v,w,c):
    penup()
    goto(x,y)
    begin_fill()
    color(c,c)
    pendown()
    for i in range(2):
        forward(w)
        left(90)
        forward(v)
        left(90)
    end_fill()
def draw_bar_char():
    l=[50,200,150,70,25,125]
    x=0
    for i in l:
        x=x+30
        v=i
        y=0
        w=15
        c="red"
        draw_bar(x,y,v,w,c)
draw_bar_char()
