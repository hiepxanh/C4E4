##1
from turtle import*
speed(0)
def draw_square(length,colour):
    
    color(colour,"white")
    begin_fill()
    for x in range (4):
        forward(length)
        left(90)
    end_fill()
draw_square(100,"green")

##2
for i in range(30):
    draw_square(i*5,"red")
    left(17)
    penup()
    forward(i*2)
    pendown()

##3
def draw_star(x,y,length):
    goto(x,y)
    for z in range(5):
        forward(length)
        left(144)
draw_star(5,10,100)

##4
speed(0)
color('blue')
for i in range(100):
    import random
    x=random.randint(-300,300)
    y=random.randint(-300,300)
    length=random.randint(3,10)
    draw_star(x,y,length)
##random.randint choose a random interger in range x-y

##5
def remove_dollar_sign(s):
    s.replace('$',"")
    return s.replace('$',"")
##6
string_with_no_dollar= remove_dollar_sign('$80% percent of $life is showing $up')
if string_with_no_dollar== '80% percent of life is showing up':
    print('Your function is correct')
else:
    print('Oops, there is a bug')

##7
def extract_even(l):
    for a in l:
        if a % 2 != 0:
            l.remove(a)
    return l
##8
even_list = extract_even([1,2,5,-10,9,6])
if set(even_list) == set([2,-10,6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
      
