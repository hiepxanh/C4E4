file = open("name_list.txt")
for line in file:
    l= line.strip().split(" ")
    print ("Hello", l[-1] + ", happy coding")
