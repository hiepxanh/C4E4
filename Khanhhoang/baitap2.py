from turtle import*
# 2 Write a program that calculates the ​ area​ of a ​ circle
radius = int(input('radius :'))
area = (radius**2)*3.14
print(area)
#3 Write a program that converts ​Celsius​in to ​Fahrenheit​
c = int(input('celsiusin :'))
f = (c*1.8)+32
print(f)
# 4
b = int(input('initial B bacteria number :'))
time = int(input('time :'))
b_later = b*(2**(time//2))
print(b_later)
