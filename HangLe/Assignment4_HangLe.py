####Assignment4:
from turtle import *
#1.

def draw_square(length, color):
    pencolor(str(color))
    forward(length)
    left(90)
    forward(length)
    left(90)
    forward(length)
    left(90)
    forward(length)
    

draw_square(100,"red")

#2.

for i in range(30):
 draw_square(i * 5, 'red')
 left(17)
 penup()
 forward(i * 2)
 pendown()


#3.
def draw_star(x,y,length):
    penup()
    goto(x,y)
    pendown()
    left(180-144)
    forward(length)
    left(144)
    forward(length)
    left(144)
    forward(length)
    left(144)
    forward(length)
    left(144)
    forward(length)
draw_star(60,40,100)

#4.
speed(0)
color('blue')
for i in range(100):
     import random
     x = random.randint(-300, 300)
     y = random.randint(-300, 300)
     length = random.randint(3, 10)
     draw_star(x, y, length)

#The random.randint() statement generates random number from a range mentioned inside the parenthesis.

##5.

def remove_dollar_sign(s):
    s=s.replace("$","")
    print(s)
    return(s)


remove_dollar_sign("hanglee$superkute")    
     
##6.
string_with_no_dollars = remove_dollar_sign("$80% percent of $life is showing $up")
if string_with_no_dollars == "80% percent of life is showing up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")


##7.
def extract_even(L):
    L1=[]
    for element in L:
        if element%2==0:
            L1.append(element)
    print(L1)
    return(L1)

            
extract_even([4,5,6])

#8.
even_list = extract_even([1, 2, 5, -10, 9, 6])
if set(even_list) == set([2, -10, 6]):
 print("Your function is correct")
else:
 print("Ooops, bugs detected")

 
