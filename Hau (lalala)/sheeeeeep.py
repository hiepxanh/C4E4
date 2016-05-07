size=[5,7,300,90,24,50,75]
print('Hello, my name is Hau and here is my flock: ')
print(size)
flock=0
size.sort()
print('now my largest sheep has size of ', max(size))
for y in range(4):
    size.sort()
    print('now after '+str(y+1)+' month my largest sheep has size of '+str(max(size)))
    flock=flock+max(size)
    print(size)
    size.append(8)
    del size[len(size)-2]
    for x in range (len(size)):
        size[x]=size[x]+50
    
print('you got '+str(flock)+'*2$='+str(flock*2)+ ' after 4 month by '+str(flock)+' flock')

