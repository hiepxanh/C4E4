r=10
pi=3.14
s=pi*r**2
print("area =%d" %(s))

oC =10
oF = oC*9/5+32
print("%d oC = %d oF" %(oC, oF))

No = 2
time = 6
result = No**(1+time//2)
print("after %d minutes we would have %d bacterias" %(No,result))

n=3
def fib(n):
    if n ==1:
        return 1
    else:
        return (n-2)+(n-1)
    
    
print ("month %d:%d pair(s) of rabbits" %(n,fib(n)))
