###1. List of String
#1.1
My_color_list = ["Blue","Red","Black","Pink","Brown","Yellow"]
print("My color list", "\n", My_color_list)

#1.2.
print("color_list at index 3",":",My_color_list[3])

#1.3.
print(My_color_list)
print(My_color_list[0])
print(My_color_list[1])
print(My_color_list[2])
print(My_color_list[3])
print(My_color_list[4])
print(My_color_list[5])

#1.4.
n=input("What is your favorite color?")
if str(n) in My_color_list:
    print("Your color is at index ",My_color_list.index(str(n))," in my list")
else:
    print("Sorry, I could not find your color")

###2. List of Numbers
#2.1.
list=[5,7,300,90,24,50,75]
print("Hello, my name is Hang and these are my sheep sizes","\n", list)

#2.2.
print("Now my biggest sheep has size ", max(list)," let's shear it")

#2.3.
list[list.index(max(list))]=8
print("After shearing, here is my flock","\n",list)

#2.4
new_list = [x+50 for x in list]
print("One month has passed, now here is my flock","\n",new_list)

#2.5.
list=[5,7,300,90,24,50,75]
print("Hello, my name is Hang and these are my sheep sizes","\n", list)
for t in range(1,4):
    print("MONTH",t,":")
    list = [x+50 for x in list]
    print("One month has passed, now here is my flock","\n",list)
    print("Now my biggest sheep has size ", max(list)," let's shear it")
    list[list.index(max(list))]=8
    print("After shearing, here is my flock","\n",list)

#2.6.
list=[5,7,300,90,24,50,75]
print("Hello, my name is Hang and these are my sheep sizes","\n", list)
print("Now my biggest sheep has size ", max(list)," let's shear it")
list[list.index(max(list))]=8
print("After shearing, here is my flock","\n",list)
for t in range(1,3):
    print("MONTH",t,":")
    list = [x+50 for x in list]
    print("One month has passed, now here is my flock","\n",list)
    print("Now my biggest sheep has size ", max(list)," let's shear it")
    list[list.index(max(list))]=8
    print("After shearing, here is my flock","\n",list)
list = [x+50 for x in list]
print("My flock has size in total:", sum(list))
print("I would get", sum(list)," *2$ = ", sum(list)*2,"$")

##3. Range
range1=range(0,7)
for each_item in range1:
    print(each_item)

range2=range(1,13,3)
for each_item in range2:
    print(each_item)
range3=range(5,0,-1)
for each_item in range3:
    print(each_item)
range4=range(6,-4,-2)
for each_item in range4:
    print(each_item)

##4. Range of numbers
#4.1
#4.2.
