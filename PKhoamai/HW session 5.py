
def salary(x,y):
    return x*y
file = open("Luong.txt")
for line in file:
    l = line.strip().split(" ")
    salary = int(l[1])*int(l[2])
    l.append(salary)
    print(l)
