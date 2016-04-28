b=input("Enter the initial B bacterial number")
t=input("Enter the period of time (in minute)")
c=int(t)/2
n=int(b)*(2**int(c))
print("After ",t," minutes, we would have ",n," bacterias")
