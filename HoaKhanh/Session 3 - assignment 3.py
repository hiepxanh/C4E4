#1. List of strings
#Color list
mycolor = ['Blue','Red','Purple','Black','Pink','Brown','Yellow']
print(mycolor)
print(mycolor[3])
for color in mycolor:
    print(color)
x = input('What is your favorite color ? ')
if x in mycolor:
    y = mycolor.index(x)
    print(str.format('You color is at index {0} in my list',y))
else:
    print('Sorry, I could not find your color')

#2. List of numbers
sizes = [2,7,98,5,9,78,56,34,14,34]
print('Hello, my name is Khanh and these are my sheep sizes:')
print(sizes)

for i in range(4):
    sizes = [50*(i+1) + x for x in sizes]
    print(i+1,'month(s) has passed, now here is my flock:')
    print(sizes)
    m = max(sizes)
    print("Now my biggest sheep has size",m, "let's shear it !")
    m_index = sizes.index(m)
    sizes[m_index] = 8
    print('After shearing, here is my flock:')
    print(sizes)

s = sum(sizes)
print('My flock has size in total: ',s)
print('I would get',s,'* 2$ = ',s*2,'$')

#3. Range
range1 = range(7)
for x in range1:
    print(x)
range2 = range(1,11,3)
for x in range2:
    print(x)
range3 = range(5,0,-1)
for x in range3:
    print(x)
range4 = range(6,-3,-2)
for x in range4:
    print(x)

#4. Range of numbers:
n = input('Input n: ')
list = []
list.extend(range(1,int(n)+1)) #creating a list with integer elements ranging from 1 to n
#4.2 & 4.3
list1 = [1/x for x in list] #creating a list consisting reciprocals of the initial list
print(list1)
s1 = sum(list1)
print(s1)
#4.4
from math import factorial
list2 = [1/factorial(x) for x in list] #creating a list consisting reciprocals of the factorials of n
print(list2)
s2 = sum(list2)
print(s2)
    
