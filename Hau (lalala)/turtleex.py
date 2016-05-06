from turtle import*
##def draw_square(length,col):#int,str
##    color(col)
##    for i in range(4):
##        forward(length)
##        left(90)
##for i in range(30):
##        draw_square(i * 5, 'red')
##        left(17)
##        penup()
##        forward(i * 2)
##        pendown()

##def stardraw(x,y,length):#int,int,int
##    penup()
##    goto(x,y)
##    pendown()
##    for i in range(5):
##        forward(length)
##        left(144)
##stardraw(20,-40,30)
##speed(0)
##color('blue')
##for i in range(100):
##    import random#import random lib
##    x = random.randint(-300, 300)#random.randint(<min>,<max>)
##    y = random.randint(-300, 300)
##    length = random.randint(3, 10)
##    stardraw(x, y, length)
def  get_even_list(numblist):#list
    a=0
    for x in numblist:
        if x%2==1:
            del numblist[a]
        a=a+1    
    return numblist
a=[1, 2, 5, -10, 9, 6]
even_list = get_even_list(a)
if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
##def remove_dollar_sign(string):
##    a=string.split('$')
##    string=''.join(a)
##    return string
##
##string_with_no_dollars = remove_dollar_sign("$80% percent of $life is showing $up")
##if string_with_no_dollars == "80% percent of life is showing up":
##    print("Your function is correct")
##else:
##    print("Oops, there's a bug")



