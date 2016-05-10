file = open('ss5_data.txt')
new = open('new_file.txt','w')
for line in file:
    l = line.strip().split(" ")
    wage = int(l[1])*int(l[2])
    l.append(str(wage))
    l_new = str(l)
    new.write(l_new+'\n')
new.close()
    
