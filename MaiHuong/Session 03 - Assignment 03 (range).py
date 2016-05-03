from turtle import *

## RANGE

range1 = range(0,7)
for each_item in range1:
    print(each_item)
my_list1 = []
my_list1.extend(range1)
print(my_list1)
print("Sum_range1 = ",sum(range1))

range2 = range(1,11,3)
for each_item in range2:
    print(each_item)
my_list2 = []
my_list2.extend(range2)
print(my_list2)
print("Sum_range2 = ", sum(range2))

range3 = range(5,0,-1)
for each_item in range3:
    print(each_item)
my_list3 = []
my_list3.extend(range3)
print(my_list3)
print("Sum_range3 = ", sum(range3))

range4 = range(6, -3, -2)
for each_item in range4:
    print(each_item)
my_list4 = []
my_list4.extend(range4)
print(my_list4)
print("Sum_range4 = ",sum(range4))


