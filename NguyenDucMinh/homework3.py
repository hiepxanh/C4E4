##Question1.1:

l=['Blue','Red','Black','Pink','Brown','Yellow']
print("My color list ",l)

##Question 1.2:
print(str.format("color_list at index 3: {0}",l[3]))

##Question 1.3:
print(l)
print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[4])
print(l[5])

#question 1.4:
t=0
color = str(input('what is your favorite color? '))
for i in l:
    if(i==color):
        t=t+1
    else:
        t=t
if(t>0):
    print(str.format('your color is at index {0} in my list',l.index(color)))
else:
    print('Sorry, I could not find your color ')
    
##Question 2.1:
l=[5,7,300,90,24,50,75]
print(str.format('Hello, my name is Hiep and these are my sheep sizes {0}',l))

##Question 2.2:
print (str.format("Now my biggest sheep has size {0} let's shear it",max(l)))

##Question 2.3:
l[2]=8
print (str.format("After shearing, here is my flock {0}",l))

##Question 2.4:
l=[5,7,300,90,24,50,75]
print(str.format('Hello, my name is Hiep and here is my flock {0}',l))
newlist=[50+ name for name in l]
print (str.format('Month 1: One month has passed, now here is my flock {0}.',newlist))

##Question 2.5:
l = [5,7,300,90,24,50,75]
print("Hello, my name is Hiep and here is my flock ", l)
n = int(input("Month(s): "))   
for t in range(1, n+1):
    print("MONTH ", t, ":")
    l = [50 + size for size in l]
    print("One month has passed and here is my flock", l)
    print("Now my biggest sheep has size", max(l), "let's sheer it")
    max_size_index = l.index(max(l))
    l[max_size_index] = 8
    print("After shearing, here is my flock", l)

##Question 2.6:
l = [5,7,300,90,24,50,75]
print("Hello, my name is Hiep and here is my flock ", l)
n = int(input("Month(s): "))   
for t in range(1, n+1):
    print("MONTH ", t, ":")
    l = [50 + size for size in l]
    print("One month has passed and here is my flock", l)
    if t == n:
        print("Flock has sizes in total: ", sum(l))
        print(str.format("I would has {0} * 2$ = {1}", sum(l), sum(l) * 2))
    else:
        print("Now my biggest sheep has size", max(l), "let's sheer it")
        max_size_index = l.index(max(l))
        l[max_size_index] = 8
        print("After shearing, here is my flock", l)



    
    
    
    


 
                  



    
    
    

 
        
        



