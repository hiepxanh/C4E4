#check a variable's type : type(x) --> <class ''>
#3 different examples of invalid names: 1hoang
#                                       hoang#
#                                       from
from turtle import*
# 2 Write a program that calculates the ​ area​ of a ​ circle
radius = int(input('radius :'))
area = (radius**2)*3.14
print('Are = ',area)
#3 Write a program that converts ​Celsius​in to ​Fahrenheit​
c = int(input('celsiusin :'))
f = (c*1.8)+32
print(f)
# 4
b = int(input('initial B bacteria number :'))
time = int(input('time :'))
b_later = b*(2**(time//2))
print(b_later)
#5 Happy Farm
m1=1
m2=2
month=int(input('month :'))
for month in range(month):
    temp = m1
    m1=m2
    m2=temp+b
print(m2)
