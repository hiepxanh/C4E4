sheep=[5,7,300,90,24,50,75]
print('Hello, my name is Giang and this is my sheep sizes')
print(sheep)
print('Now my biggest sheep has size',max(sheep),'lets shear it')
print("After shearing, here is my flock:")
sheep.append(8)
sheep.remove(max(sheep))
print("After shearing, here is my flock:")
print(sheep)
