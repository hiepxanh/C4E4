list=[5,7,300,90,24,50,75]
print('Hello, my name is Tung and these are my ship sizes')
print(list)
print("Now my biggest sheep has size ",max(list),"let 's shear it")
list.insert(2,8)
list.remove(max(list))
print("After shearing,here is my flock")
print(list)
list=[50+size for size in list]
print('One month has passed , now here is my flock')
print(list)
