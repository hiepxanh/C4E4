from turtle import*
speed(0)
#1+2
def draw_square(length,colr):
    color(colr)
    for i in range(4):
        forward(length)
        left(360/4)
for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

#3+4
def draw_star(x,y,length):
    penup()
    goto(x,y)
    pendown()
    for i in range(5):
        forward(length)
        left(144)
speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    length = random.randint(3,10)
    draw_star(x,y,length)
#Random.randint: Return a random integer N such that a <= N <= b.

#5+6
def remove_dollar_sign(s):
    s = str(s)
    s_replace = s.replace("$","")
    return s_replace
s = input("Input dollar to replace: ")
print("Result:",remove_dollar_sign(s))

string_with_no_dollar = remove_dollar_sign("80% percent of $life is showing $up")
if string_with_no_dollar == "80% percent of life is showing up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")
    
#7+8
l = [1,4,5,-1,10]
def get_even_list(l):
    for each_number in l:
        if each_number % 2 != 0:
            l.remove(each_number)
    return l

even_list = get_even_list([1,2,5,-10,9,6])
if set(even_list) == set([2,-10,6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")





