##1.check a variable's type: type(variable)
##Invalid variable names include:
##    - names beginning with numbers: 1xyz
##    - contain special characters: xyz#
##    - Python keywords: global
##2. Area of a circle
print("Calculate the area of a circle")
r = int(input("What's the radius of the circle ? "))
print("Area = ",3.14*r**2)
##3. Convert Celsius into Fahrenheit
print("Convert Celsius into Fahrenheit")
c = int(input("Input the temperature in Celsius "))
f = c*1.8+32
print(c," (C) = ",f," (F)")
##4. Calculate the number of bacteria after a period of time
print("Calculate the number of bacteria after a period of time")
b1 = int(input("Input the initial number of bacteria "))
t = int(input("Input the period of time (in minutes) "))
b2 = b1*2**(t/2)
print(str.format("After {0} minutes we would have {1} bacteria",t,b2))
##5. The number of rabbits after 4 months
a = 0
b = 1
for x in range(5):  
        a,b = b,a+b
        print(str.format("Month {0} : {1} pair(s) of rabbits", x, b))
#thu edit phat
    
    
