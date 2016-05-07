##1
from turtle import*
speed(0)
shape("turtle")
def draw_square(x,y):
    begin_fill()
    for i in range(4):
        forward(100)
        left(90)
    color(y,'white')
    end_fill()
draw_square(200,"black")
##2
for i in range(30):
    draw_square(i*5,'red')
    left(17)
    penup()
    forward(i*2)
    pendown()
##3
def draw_star(x,y,length):
    goto(x,y)
    pendown()
    color('black','pink')
    begin_fill()
    for i in range(6):
        forward(length)
        left(144)
    end_fill
    penup()
draw_star(20,30,50)
##4
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)
##5
def remove_dollar_sign(s):
    s.replace('$',"")
    return s.replace('$',"")
##6
string_with_no_dollars = remove_dollar_sign("$80% percent of $life is showing $up")
if string_with_no_dollars == "80% percent of life is showing up":
    print("Your function is correct\n")
else:
    print("Oops, there's a bug")
##7
def extract_even(l):
    for i in l:
        if i%2!=0:
            l.remove(i)
    return l
##8
even_list = extract_even([1, 2, 5, -10, 9, 6])
if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
        
