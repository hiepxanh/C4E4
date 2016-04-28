## BÀI LÀM ÐUOC THAM KHAO TU MOT SO BAN 
   ##1. - To check variable's type: type in shell: type(X), then the output will be: class Y which Y is the type.
   ###  - SyntaxError happens when:
   ###    begin with number: 7up
   ###    illegal character: hoa@
   ###    keywords: and
   ##2. Calculate area of a circle
from turtle import *
Radius=10
Area=(Radius**2)*3.14
print("Radius?",Radius)
print("Area = ",Area)
   ##3. Converts Celsius (C) into Fahrenheit (F)
C=10
F=C*9/5+32
print("Enter the temperature in Celsius", C)
print(C,"(C) =",F,"(F)")
   ##4.
B=2
Time=4
Total=B*(2**(Time//2))
print("How many B bacterias are there?",B)
print("How much time will we wait?",Time)
print("After",Time,"minutes we would have",Total,"bacterias")
   ##5
P=1
S=0
print("Month",0,":",P,"pair(s) of rabbits")
for x in range(1,4):
    P=P+S
    S=P-S
    print("Month",x,":",P,"pair(s) of rabbits")
