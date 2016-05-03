##BAI 1
L=['Blue','Red','Black','Pink','Brown','Yellow']

print('My color list')
print(L)
print("--")

print("color_list at index 3:",L[3])
print("--")

for x in L:
    print(str.format(x))
print("--")

InputColor = input("What is your favorite color? ")
x = str(InputColor)
for x in L:
    if InputColor == str.format(x):
        print("Your color is at index",L.index(x),"in my list")
if InputColor not in L:
    print("Sorry, I could not find your color")
print("--")

##BAI 2
N=[5,7,300,90,24,50,75]
print("Hello, my name is Hoanh and these are my sheep sizes:")
print(N)
print(" ")

print("Now my biggest sheep has size",max(N),"let shear it")
print(" ")

print("After shearing, here is my flock:")
N.append(8)
N.remove(max(N))
print(N)
print(" ")

for month in range(1,4):
    print("MONTH",month)
    print("One month has passed, now here is my flock:")
    for x in range(7):
        N[x]=N[x]+50
    print(N)
    print(" ")
    Tong = sum(N)
    Money = Tong*2
    print("My flock has size in total:",Tong)
    print("I would get",Tong,"*2$ =",Money,"$")
    print(" ")
    print("After shearing, here is my flock:")
    print("Now my biggest sheep has size",max(N),"let shear it")
    N.append(8)
    N.remove(max(N))
    print(N)
    print(" ")
print("--")

##BAI 3
a = range(7)
b = []
b.extend(a)
print("range1:",b)
c= range(1,11,3)
d = []
d.extend(c)
print("range2:",d)
e= range(5,0,-1)
f= []
f.extend(e)
print("range3:",f)
g= range(6,-3,-2)
h= []
h.extend(g)
print("range4:",h)
print("--")

##BAI 4
n = input("Nhap n=")
n = int(n)
S1=0
for i in range(1,n+1):
    S1=S1+(1/i)
if n==1:
    print("S1 = S2 = 1")
else:
    print("S1 = ",S1)
