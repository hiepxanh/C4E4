list = ["Blue", "red", "black", "pink", "brown", "yellow"]
print ("my color list",list)

print("color_list at index 3:",list[3])

print(list)

for name in list:
    print(name)

a = "red"
if a in list:
    print("what is your favorite color?",a,"\n","your color is at index",list.index(a),"in my list")
else:
    print("what is your favorite color?",a,"Sorry, I could not find your color")

sheep_size = [25,8,89,90,100]
print("Hello, my name is PK and these are my sheep sizes","\n",sheep_size)

print("Hello, my name is PK and these are my sheep sizes","\n",sheep_size,"\n", "now biggest sheep has size",max(sheep_size), "let's shear it")
sheep_size[sheep_size.index(max(sheep_size))]=8
print("After shearing, here is my flock", "\n",sheep_size)

New_sheep_size = [x+50 for x in sheep_size]
print("One month has passed, now here is my flock",New_sheep_size)

##2.5
for t in range(1,4):
        print("Month",t)
        sheep_size =[x+50 for x in sheep_size]
        print("One month has passed, now here is my flock","\n",sheep_size)
        print("Now my biggest sheep has size",max(sheep_size),"let shear it")
        sheep_size[sheep_size.index(max(sheep_size))]=8
        print("After shearing, here is my flock","\n",sheep_size)

##2.6
for t in range(1,3):
        print("Month",t)
        sheep_size =[x+50 for x in sheep_size]
        print("One month has passed, now here is my flock","\n",sheep_size)
        print("Now my biggest sheep has size",max(sheep_size),"let shear it")
        sheep_size[sheep_size.index(max(sheep_size))]=8
        print("After shearing, here is my flock","\n",sheep_size)

print("Month",3)
sheep_size =[x+50 for x in sheep_size]
print("One month has passed, now here is my flock","\n",sheep_size)
print("My flock hasa size in total:", sum(sheep_size),"\n", "Iwould get",sum(sheep_size),"*2$=",sum(sheep_size)*2,"$")
##3
range1=range(0,7)
for x in range1:
    print(x,end=", ")
print("\n")
    
range2 = range(1,11,3)

for x in range2:
    print(x,end=", ")
print("\n")
range3 = range(5,0,-1)
for x in range3:
    print(x,end=", ")
print("\n")
range4 = range(6,-3,-2)
for x in range4:
    print(x,end=", ")

##4
n=10
S=1/n+1/(n+1)
for n in range (1,10):
    print(sum(s))

