list=[5,7,300,90,24,50,75]
print('Hello, my name is Tung and here is my flock')
print(list)
n=input('Month:')
for x in range(1,int(n)+1):
    print('Month',int(x))
    list=[50+size for size in list]
    print("One month ha passed , now here is my flock")
    print(list)
    print(str.format("Now my biggest sheep has size {0} let's shear it",max(list)))
    print("After shearting , here is my flock")
    list.remove(max(list))
    list.insert(2,8)
    print(list)


        
        
