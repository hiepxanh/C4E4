##1
from turtle import*
def draw_square(a,b):
    begin_fill()
    for i in range(4):
        color(b,"pink")
        forward(a)
        left(90)
    end_fill()
draw_square(100,"red")
##2
for i in range(30):
    draw_square(i*5,'red')
    left(17)
    penup()
    forward(i*2)
    pendown()
##3
from turtle import*
def draw_star(x,y,length):
    penup()
    goto(x,y)
    for i in range(5):
        pendown()
        forward(length)
        left(144)
draw_star(10,50,100)
##4
speed(0)
color('blue')
for i in range(100):
    import random
    x=random.randint(-300,300)
    y=random.randint(-300,300)
    length=random.randint(3,10)
    draw_star(x,y,length)
##5
def remove_dollar_sign(str):
    str.replace('$',"")
    return str.replace('$',"")
##6
string_with_no_dollars = remove_dollar_sign("$80% percent of $life is showing $up")
if string_with_no_dollars == "80% percent of life is showing up":
    print("your function is correct")
else:
    print("Oops, there's a bug")
