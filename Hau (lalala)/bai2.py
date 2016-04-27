##x="lalala"
##type(x)#type check
##    #invalid name:209FA, *lalala, float
##        #circle area
##xr=input("radius: ")
##radius=int(xr)
##print("Area =",radius**2*3.1412)
##        #c(0)->f(0)
##xr=input("temperature in C:")
##c=int(xr)
##print(str.format('temperature in F: 10*C ={0}*F',c*1.8+32 ))
##        #so vi khuan
##xr=input("Minute?")
##time=int(xr)
##print(str.format("after {0} have {1} bacteria",xr,2**time//2))
        #chuoi fibonacci
a=0
b=1
k=0
xr=input("time")
time=int(xr)
for x in range (time):
    k=a
    a=b+a
    b=k
    print(",",a)
