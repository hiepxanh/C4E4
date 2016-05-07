from turtle import *

# Exercise 1
## Check variables type: type ()

a=1
b=1.06
c="Moon" 

print(type(a)) 
print(type(b)) 
print(type(c))

## 3 examples of invalid name
## 123abc = 13
## yahoo@= "hello"
## for = 21

# Exercise 2: Area of the circle
r = 10 # r : radius
area = r**2*3.14
print(" Area = ", area)

# Exercise 3: Convert Celsius to Fahrenheit
# Fahrenheit = Celsius *1.8 + 32

C=10
F=C*1.8+32
print(str.format("{0}(C) = {1}(F)", C, F))

# Exercise 4: Bacterias
B = 2 #initial B bacteria number
T = 4 #time in minutes

total=B*(2**(T//2))
print("After","4 minutes we would have", total, "bacterias")

# Exercise 5: Happy Farm
a=0
b=1
for x in range (5):
    a,b = b, a+b
    print(str.format("Month {0}: {1} pair(s) of rabbits", x,b))
    

