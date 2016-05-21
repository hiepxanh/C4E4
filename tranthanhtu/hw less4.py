####1.
##from turtle import *
##f= int(input("f="))
##c= str(input("c ="))
##def draw_square(f,C):
##    color(c,"white")
##    for x in range(4):
##        forward(f)
##        left(90)
##print(draw_square)
##draw_square(f,c)
##
##    
###2.
##for i in range(30):
##    draw_square(i*5,'red')
##    left(17)
##    penup()
##    forward(i*2)
##    pendown()
##3.
from turtle import *
##
##def draw_star(x,y,l):
##    penup()
##    goto(x,y)
##    pendown()
##    for i in range(5):
##        right(144)
##        forward(l)
##print(draw_star)
##4.
##x = int(input("x="))
##y = int(input("y="))
##l = int(input("l="))
##draw_star(x,y,l)
##
##color("blue")
##for i in range(100):
##    import random
##    x = random.randint(-300,300)## lua chon ngau nhien gia tri trong khoang (x,y)
##    y = random.randint(-300,300)
##    l = random.randint(3,10)
##    draw_star(x,y,l)
##5.
##a = "$80% percent of $life is showing up"
##def remove_dollar_sign(a):
##    remove_dollar_sign = a.replace("$","")
##    return remove_dollar_sign
##remove_dollar_sign(a)
###6.
##string_with_no_dollars = remove_dollar_sign("$80% percent of $life is showing up")
##if string_with_no_dollars == "80% percent of life is showing up":
##    print("Your function is correct")
##else:
##    print("Oops, there's a bug")

#7.
number_list=[1,4,5, -1,10]
def  get_even_list(number_list):
    l = 0
    for x in number_list:
        if x%2==1:
            del number_list[l]
        l = l+1
    return number_list
b = get_even_list(number_list)
print(b)
a=[1, 2, 5, -10, 9, 6]
even_list = get_even_list(a)
print (even_list)
if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
