##def calculator(x,y,s):
##    s = str(s)
##    if s == "+":
##        return x+y
##    if s == "-":
##        return x-y
##    if s == "*":
##        return x*y
##    if s == "/":
##        return x/y
##
##x = int(input("x = "))
##y = int(input("y = "))
##s = input("s = ")
##print(calculator(x,y,s))

##import time
##import turtle
##import webbrowser
##x = webbrowser.open("https://www.youtube.com/watch?v=c4BLVznuWnU")
##x = turtle.penup()
##print(x)
##time.sleep(3)
##print("Hello World")
##print(webbrowser.__file__)


from turtle import*
##def draw_bar(x,y,v,w,c):
##    color(c,c)
##    penup()
##    goto(x,y)
##    pendown()
##    begin_fill()
##    for i in range(2):
##        forward(w)
##        left(90)
##        forward(v)
##        left(90)
##    end_fill()


def draw_bar(x,y,v,w,c):
    color(c,c)
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    for i in range(2):
        forward(w)
        left(90)
        forward(v)
        left(90)
    end_fill()    

def bar_chart(l):
    g=0
    for x in l:
        g=g+30
        draw_bar(g,0,x,15,"red")

l = [50,200,150,70,25,125]

bar_chart(l)


