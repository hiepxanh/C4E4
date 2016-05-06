##4.2
a=0
for x in range(1,11):
    a=a+1/x
print(a)
##4.3
n=input('n:')
a=0
for n in range(1,int(n)+1):
    a=1+1/int(n)
print(a)
##4.4
n=input('n:')
a=1
b=0
for n in range(1,int(n)+1):
    a=a*int(n)
    b=b+1/a
print(b)
