#1.1

l=["Blue", "Red", "Black", "Pink", "Brown", "Yellow"]
print(str.format("My color list {0}", (l))) 



#1.2
print(str.format("color_list at index 3: {0}", l[-3]))



#1.3
l=["Blue", "Red", "Black", "Pink", "Brown", "Yellow"]
print(l)

l=["Blue", "Red", "Black", "Pink", "Brown", "Yellow"]
for line in l:
    l=line.split (" ")
    print(l)


    
#1.4
l=["Blue", "Red", "Black", "Pink", "Brown", "Yellow"]
a="Red" #or a = "Green" 
print(str.format("What is your favorite color? {0}", a))

if a == l[1]:
    n=l.index("Red")
    print(str.format("Your color is at index {0} in my list", n))
else:
    print("Sorry, I could not find your color") 
    


#2.1
list=["5", "7", "300", "90", "24", "50", "75"]
print(str.format("Hello, my name is Hiep and these are my ship sizes {0}", list))



#2.2
print(str.format("Hello, my name is Hiep and these are my ship sizes {0}", list))
list=[int(i) for i in list]
m=max(list)
print(str.format("Now my biggest sheep has size {0} let's shear it", m))



#2.3
print(str.format("Hello, my name is Hiep and these are my ship sizes {0}", list))
list=[int(i) for i in list]
m=max(list)
print(str.format("Now my biggest sheep has size {0} let's shear it", m))
list.insert(list.index(m), int(8))
list.remove(m)
print(str.format("After shearing, here is my flock {0}", list))



#2.4 
print(str.format("Hello, my name is Hiep and these are my ship sizes {0}", list))
list=[int(i) for i in list]
m=max(list)
print(str.format("Now my biggest sheep has size {0} let's shear it", m))
list.insert(list.index(m), int(8))
list.remove(m)
print(str.format("After shearing, here is my flock {0}", list))


for index in range(len(list)):
	list[index] = str(int(list[index]) + 50)

print(str.format("One month has passed, now here is my flock {0}", list))


   
#2.5
print(str.format("Hello, my name is Hiep and these are my ship sizes {0}", list))
for x in range(1,4):
    print(str.format("Month {0} :", x))
    for index in range(len(list)):
        list[index] = str(int(list[index]) + 50)
    print(str.format("One month has passed, now here is my flock {0}", list))
    list=[int(i) for i in list]
    m=max(list)
    print(str.format("Now my biggest sheep has size {0} let's shear it", m))
    list.insert(list.index(m), int(8))
    list.remove(m)
    print(str.format("After shearing, here is my flock {0}", list))



#2.6
print(str.format("Hello, my name is Hiep and here is my flock {0}", list))
list=[int(i) for i in list]
m=max(list)
print(str.format("Now my biggest sheep has size {0} let's shear it", m))
list.insert(list.index(m), int(8))
list.remove(m)
print(str.format("After shearing, here is my flock {0}", list))

for x in range(1,3):
    print(str.format("Month {0} :", x))
    for index in range(len(list)):
        list[index] = str(int(list[index]) + 50)
    print(str.format("One month has passed, now here is my flock {0}", list))
    list=[int(i) for i in list]
    m=max(list)
    print(str.format("Now my biggest sheep has size {0} let's shear it", m))
    list.insert(list.index(m), int(8))
    list.remove(m)
    print(str.format("After shearing, here is my flock {0}", list))

print("Month 3 :")
for index in range(len(list)):
    list[index] = str(int(list[index]) + 50)
print(str.format("One month has passed, now here is my flock {0}", list))

list=[int(i) for i in list]
total=sum(list)      
print(str.format("My flock has size in total: {0}", total))
money=total*2
print(str.format("I would get {0} * 2$ = {1}$", total, money))



#3
list1=range(0,7)
range1=[]
range1.extend(list1)
print(str.format("range1 {0}", range1))

list2=range(1,11,3)
range2=[]
range2.extend(list2)
print(str.format("range2 {0}", range2))

list3=range(5,0,-1)
range3=[]
range3.extend(list3)
print(str.format("range3 {0}", range3))

list4=range(6,-3,-2)
range4=[]
range4.extend(list4)
print(str.format("range4 {0}", range4))


#4.2


#4.3


#4.4

