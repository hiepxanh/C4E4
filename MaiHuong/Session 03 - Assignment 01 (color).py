from turtle import *
color_list = ['Blue', 'Red', 'Black', 'Pink', 'Brown', 'Yellow']
# Exercise 1.1: print out list
print("My color list " , color_list)

# Exercise 1.2: print out color list at index 3
color_index_3 = print("Color_list at index 3: " + color_list[3])

# Excercise 1.3: print out color list in two way
print(color_list)
for each_color in color_list:
    print(each_color)

# Exercise 1.4: check if a color is in color list

x = input("What is your favorite color?: ")

if x in color_list:
    print("Your color is at index", color_list.index(str(x)),"in my list")
else:
    print("Sorry, I could not find your color")



    







