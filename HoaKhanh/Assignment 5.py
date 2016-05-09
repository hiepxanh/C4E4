file = open('ss5_data.txt')
for line in file:
##    print(line)
    l = line.strip().split(" ")
    wage = int(l[1])*int(l[2])
    l.append(wage)
    print(l)
