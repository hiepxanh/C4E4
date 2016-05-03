sheep=[5,7,300,90,24,50,75]
print('Hello, my name is Giang and this is my sheep sizes')
print(sheep)
print(" ")
print('Now my biggest sheep has size',max(sheep),'lets shear it')
sheep.append(8)
sheep.remove(max(sheep))
print(" ")
print("After shearing, here is my flock:")
print(sheep)
print(" ")

for x in range(7):
    sheep[x]=sheep[x]+50

print('One month has passed, now here is my flock')
print(sheep)

for month in range(4):
    print('After ',month+1,' months here is my flock')
    for x in range(7):
        sheep[x]=sheep[x]+50
    print(sheep)
    print(" ")
    print('Now my biggest sheep has size ',max(sheep),'lets shear it')
    print(" ")
    sheep.append(8)
    sheep.remove(max(sheep))
    print("After shearing, here is my flock:")
    print(sheep)
    print(" ")
