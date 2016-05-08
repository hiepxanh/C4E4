from turtle import*
def draw_bar(x,y,v,w,c):
    color(c,c)
    hideturtle()
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    for i in range (2): 
        forward(w)
        left(90)
        forward(v)
        left(90)
    end_fill()  
##draw_bar(20,30,70,20,"red")
    
def draw_bar_chart(x,l):
    
    for i in l:
        draw_bar(x,0,i,30,"red")
        x+=50
l =[50,200,150,70,25,125]
draw_bar_chart(20,l)
    
