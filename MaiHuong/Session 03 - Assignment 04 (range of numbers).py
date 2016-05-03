from turtle import *
## 4.1
B1 = 0
a1 = 0

for i in range(1,10):
    a1 = 1/i
    B1 = B1 + a1
print("Tong la: ",B1)

## 4.2
B2 = 0
a2 = 0
n = int(input("Nhap gia tri: "))
for i in range (1, n+1):
    a2 = 1/i
    B2 = B2 + a2
print("Tong la: ",B2)

## 4.3
n = int(input("Nhap gia tri: "))
a = 1 
B = 0 # tong
for i in range (1, n+1):
    a = a*i
    B = B + 1/a
print("Tong day: ",B)
