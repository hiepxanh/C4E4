from turtle import *

#Turtle Exercise
#1
def draw_square(length, col):
    color(col, "white")
    begin_fill()
    for x in range(4):
        forward(length)
        left(90)
    end_fill()

draw_square(100, "blue")



#2
for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

       

#3
def draw_star(x,y,length): #int for all three
    penup()
    goto(x,y)
    pendown()
    for x in range(5):
        forward(length)
        left(144)

draw_star(10,20,50)



#4       
speed(0)
color('blue')
for i in range(100):
    import random
    x=random.randint(-300,300)
    y=random.randint(-300,300)
    length=random.randint(3,10)
    draw_star(x,y,length)

#random.randint chooses a random integer in the given range of x and y


#Serious Exercise
#5
def remove_dollar_sign(s):
    s=str(s)
    s.replace("$","")
    return s.replace("$","")

s=input("Input: ")
print(remove_dollar_sign(s))



#6
string_with_no_dollars = remove_dollar_sign("80% percent of life is showing up")

if string_with_no_dollars == "80% percentof life is showing up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")



#7
def get_even_list(l):
    for n in l:
        if n % 2 != 0:
            l.remove(n)
    return l


#8
l=[1,2,5,-10,9,6]

even_list = get_even_list(l)

if set(even_list) == set([2,-10,6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")

    
