from turtle import *

def total_digits(number):
    n = number
    result = 0
    while n != 0:
        result += n % 10
        n //= 10
    return result

# i = 2 -> n - 1

def check_prime(n):
    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False
    return prime

n = int(input("Enter a number: "))

if check_prime(n):
    print("{0} is a prime number".format(n))
else:
    print("{0} is NOT a prime number".format(n))

t = total_digits(n)
print("Total digits of {0} is {1}".format(n, t))

if check_prime(t):
    print("and it is a prime number")
else:
    print("and it is NOT a prime number")

##if check_prime(7):
##    print("P")
##else:
##    print("Not P")

##print(check_prime(7))
##if prime == 1:
##    print("Prime number")
##else:
##    print("Not a prime number")

#print(total_digits(n))


##forward(100)
##left(120)
##forward(100)
##left(120)
##forward(100)
##left(120)
##
##penup()
##goto(20,50)
##pendown()
##forward(200)
##left(120)
##forward(200)
##left(120)
##forward(200)
##left(120)
##
##penup()
##goto(60,100)
##pendown()
##forward(400)
##left(120)
##forward(400)
##left(120)
##forward(400)
##left(120)

##def draw_triangle(a, b, length):
##    penup()
##    goto(a,b)
##    pendown()
##    forward(length)
##    left(120)
##    forward(length)
##    left(120)
##    forward(length)
##    left(120)
##print(draw_triangle)
##draw_triangle(10, 20, 100)
##draw_triangle(30, 40, 200)

# 10 + 20
# 1 + 5 + 2
# 10 + 9 + 7 + 20

##def add(x,y):
##    return x + y

##add(10,20)
##
##d = add(10, 9)
##d1 = add(7, 20)
##d2 = add(d, d1)
##
##print(d2)

#print(add(add(10,9),add(7,20)))

##print(add(4,10))
##
##a = add(1, 4)
##print(a)
