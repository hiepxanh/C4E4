a=input('enter number of sheeps:')
a=int(a)
size=[]
flock=0
print('Size plz:')
for x in range(a):
    size.append(int(input(str(x)+':')))
print('what u have just entered is: ')
print(size)
for y in range(4):
    size.sort()
    print('largest is ', max(size))
    flock=flock+max(size)
    del size[len(size)-1]
    print(size)
    for x in range (len(size)):
        size[x]=size[x]+50
print('you got '+ str(flock*3)+' after 4 month by '+str(flock))

