##1.1
l= ['Blue','Red', 'Black', 'Pink', 'Brown','Yellow']
print ("My color list")
print (l)
##1.2
print ("color_list at index 3: ",l[3])
##1.3
print (l)
 #or
x =0 
n = input ("what is your favorite color?")
for name in l:
    print (name)
    if n == name:
        x=x+1
    else:
        x=x
if (x>0):
    print ("Your color is at index 1 in my list")
else:
    print ("Sorry, I could not find your color")

##2.1

n= [5,7,300,90,24,50,75]
print ("Hello, my name is Tu and there are my ship size")
print (n)
##2.2
print ("Now my biggest sheep has size", max(n)," let's shear it")
##2.3
n.remove(max(n))
print ("after shearing, here is my flock")
print (n)
##2.4
n2=[int(50) + name for name in n]
print ("Onr month has passed, now here is my flock")
print (n2)
##2.5
month = input ("month=")
nn = [(int(50)*int(month)) + name for name in n]
print (nn)
####2.6
b = sum(nn) * 2
print ("My flock has size in total: ", sum(nn))
print ("I would get ",sum(nn)," * 2$ = ", b,"$")

#3 Range

my_range= range(0,7,1)
my_list=[]
my_list.extend(my_range)
print ("Range1:", my_list)
my_range= range(1,11,3)
my_list=[]
my_list.extend(my_range)
print ("Range2:", my_list)
my_range= range(5,0,-1)
my_list=[]
my_list.extend(my_range)
print ("Range3:", my_list)
my_range= range(6,-3,-2)
my_list=[]
my_list.extend(my_range)
print ("Range4:", my_list)

#4 Range of numbers
#4.1
n= input("n=")
my_range = range(1,int(n)+1)
my_list=[]
my_list.extend(my_range)
##print (sum(my_list))
#4.2-4.3
list1 = [1/x for x in my_list]
print(list1)
print (sum(list1))




