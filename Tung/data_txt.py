file = open('ss5_data.txt')
for x in file :
    l= x.split(' ')
    a= int(l[1]) * int(l[2])
    print(str.format('After {0} hours, {1} received $ {2}',l[2],l[0],a))
    
