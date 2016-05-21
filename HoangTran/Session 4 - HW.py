BAI 1&2
from turtle import*
def draw_square(length, color):
    pencolor(color)
    for _ in range (4):
        forward(length)
        left(90)
        
draw_square(100, 'red')
speed(0)

for i in range(30):
    draw_square(i*5, 'red')
    left(17)
    penup()
    forward(i*2)
    pendown()
    
#-------------------------------------------------------------
    
BAI 3&4
from turtle import*
def draw_star(x, y, length):
    goto(x,y)
    for _ in range (5):
        forward(length)
        right(180-360/10)
draw_star(0,0,100)

speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)

#random.randint: lenh random: goto 1 diem toa do (x,y) random tu -300 den 300, Length cung lua chon random tu 3 - 10
#sau do thuc hien function draw_star voi nhung gia tri random, vong lap 100 lan.

#-------------------------------------------------------------

BAI 5&6
def remove_dollar_sign(s):
    print (s.replace("$",""))
    return s.replace("$","")

string_with_no_dollars = remove_dollar_sign("$80% percent of $life is showing $up")
if string_with_no_dollars == "80% percent of life is showing up":
     print("Your function is correct")
else:
     print("Oops, there's a bug")

#-------------------------------------------------------------
     
BAI 7&8'
def extract_even(l):
    li=[ ]
    for i in l:
        if i%2==0:
            li.append(i)
            print(li)
    return li

list=[1,4,5,6,7,8,-1,10]
extract_even(list)

even_list = extract_even([1, 2, 5, -10, 9, 6])
if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")


