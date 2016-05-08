##import webbrowser
##webbrowser.open("http://vnexpress.net/tin-tuc/khoa-hoc/hoi-dap/lam-duong-phen-the-nao-3375550.html")
##
##def calculation (a,sign,c):
##    if sign=="+":
##        return a+c
##    if sign =="-":
##        return a-c
##    if sign=="*":
##        return a*c
##    if sign =="/":
##        return a/c
##x=calculation(1,"+",2)
##print(x)
from turtle import *
def draw_bar(x,y,a,b,c):
    penup()
    goto(x,y)
    pendown()
    color(c,c)
    begin_fill()
    forward(b)
    left(90)
    forward(a)
    left(90)
    forward(b)
    left(90)
    forward(a)
    end_fill()
##draw_bar(10,20,80,20,"red")

l=[50,200,150,70,25,125]
##l=[50,200]
x=10
for a in l:
    draw_bar(x,0,a,20,"red")
    x=x+30
    left(90)
    
