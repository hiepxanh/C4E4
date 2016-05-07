#1.2
from turtle import *
##def draw_square(length,color):
##    pencolor(str(color))
##    for x in range(4):
##        forward (length)
##        left(360/4)
##for i in range(30):
## draw_square(i * 5, 'red')
## left(17)
## penup()
## forward(i * 2)
## pendown()
#3.4
##def draw_star(x,y,length):
##    penup()
##    goto(x,y)
##    pendown()
##    for i in range(5):
##        forward(length)
##        right(144)
##draw_star(10,10,100)
##speed(0)
##color('blue')
##for i in range(100):
## import random
## x = random.randint(-300, 300)
## y = random.randint(-300, 300)
## length = random.randint(3, 10)
## draw_star(x, y, length)

#5.6
##def remove_dollar_sign(s):
##    s=s.replace("$","")
##    return s
##string_with_no_dollars = remove_dollar_sign("$80% percent of $life is showing $up")
##if string_with_no_dollars == "80% percent of life is showing up":
## print("Your function is correct")
##else:
## print("Oops, there's a bug")
## 
#7.8
def extract_even(L):
    L=[x for x in L if x%2==0]
    return L

even_list = extract_even([1, 2, 5, -10, 9, 6])
if set(even_list) == set([2, -10, 6]):
 print("Your function is correct")
else:
 print("Ooops, bugs detected")
