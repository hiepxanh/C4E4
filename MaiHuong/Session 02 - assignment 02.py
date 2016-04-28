from turtle import *

# Exercise 1
## Check variables type: type ()
a = 3
b = 3.05
c = "Hello"

print(type(a))
print(type(b))
print(type(c))

## 3 examples of invalid name
##3consoi = 13
##soi@ = "hello"
##max(i) = 21

# Exercise 2: calculates areas of the circle
r = 10 # r : radius
areas = r**2*3.14
print(" Areas = ", areas)

# Exercise 3: convert Celsius​(0C) into Fahrenheit​(0F)
C = 10
F = C*1.8 + 32
print(str.format("Temperature: {0} (C) = {1} (F)", C, F))

# Exercise 4: bacterias
B = 2
for i in range (5):
    total = B*(2**(i//2))
    print("After ", i, " minutes we would have ", total, " bacterias")
    
# Exercise 5: fibonacci
a = 0
b = 1
for i in range(0, 5):  
        a,b = b, a+b
        print(str.format("Month {0} : {1} pair(s) of rabbits", i, b))




