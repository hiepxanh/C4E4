from turtle import *
#1. draw square:
def draw_square(length,line_color):
    color(line_color)
    forward(length)
    left(90)
    forward(length)
    left(90)
    forward(length)
    left(90)
    forward(length)
    left(90)
##draw_square(100,"red")
#2. Hiep's code
for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()
#3. draw a star:
def draw_star(x,y, length):
    penup()
    goto(x,y)
    pendown()
    left(72)
    forward(length)
    right(144)
    forward(length)
    right(144)
    forward(length)
    right(144)
    forward(length)
    right(144)
    forward(length)
    right(144)
##draw_star(10,20,150)
#4. Hiep's code
speed(0)
color('blue')
for i in range(100):
    import random 
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)
#5. remore $ sign:
def remove_dollar_sign(s):
    s = s.replace('$','')    
    return s
#6. Hiep's code:
string_with_no_dollars = remove_dollar_sign("$80% percent of $life is showing $up")
if string_with_no_dollars == "80% percent of life is showing up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")
#7. extract even integers
def extract_even(l):
    l = [x for x in l if x%2 == 0]
    return l
#8. Check the code:
even_list = extract_even([1, 2, 5, -10, 9, 6])
if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
