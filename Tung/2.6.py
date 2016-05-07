list=[5,7,300,90,24,50,75]
print('Hello, my name is Tung and here is my flock')
print(list)
n=input('Month:')
for x in range(1,int(n)+1):
    print('Month',int(x))
    list=[50+ size for size in list]
    print("One month ha passed , now here is my flock")
    print(list)
    if int(x)==int(n):
        print("My flock has size in total :",sum(list))
        print(str.format("I would get {0} *2$ = {1}",sum(list),sum(list)*2))
    else:
        print(str.format("Now my biggest sheep has size {0} let's shear it",max(list)))
        print("After shearting , here is my flock")
        list.remove(max(list))
        list.insert(2,8)
        print(list)
        
        
