file = open("ss5_data.txt")
for x in file:
    l = x.split(" ")
    t = int(l[1])*int(l[2])
    print(str.format("After {0} hours, {1} recieves a total of {2} USD",l[2],l[0],t))

