##1
l=['Blue','Red','Black','Pink','Brown','Yellow']
print('My color list \n',l)
##2
print('color_list at index 3: ',l[3])
##3
print(l)
for i in l:
    print(i)
##4
t=0
color = str(input('what is your favorite color? '))
for i in l:
    if(i==color):
        t=t+1
    else:
        t=t
if(t>0):
    print('your color is at index 1 in my list ')
else:
    print('Sorry, I could not find your color ')
##2.1
n=[5,7,300,90,24,50,75]
print('Hello, my name is Hoang and there are ship sizes \n',n)
##2.2
t=0
t1=0
for i in n:
    if(i>t):
        t=i
        t1=t1+1
    else:
        t=t
print('Now my biggest sheep has size',t,"let'shear it")
##2.3
if(t1!=0):
    n.remove(t)
    n.insert(t1-1,8)
print('After shearing, here is my flock \n',n)
##2.4
n_after=[50+a for a in n]
print('One month has passed, now here is my flock \n',n_after)
##2.5
n=[5,7,300,90,24,50,75]
print('Hello, My name is hoang and here is my flock\n',n)
for i in range(1,4):
    print('\n MONTH ',i,' :\n')
    n=[50+a for a in n]
    print('One month has passed, now here is my flock\n',n)
    print('Now my biggest sheep has size',max(n),"let's shear it")
    n[n.index(max(n))]=8
    print('After shearing, here is my flock \n',n)
##2.6
n=[5,7,300,90,24,50,75]
print('\n \nHello, my name is hoang and here is my flock\n',n)
print('Now my biggest sheeo has size ',max(n),"let's shear it")
n[n.index(max(n))]=8
print('After shearing, here is my flock\n',n)
for i in range(1,3):
    print('\n MONTH ',i,' :\n')
    n=[50+a for a in n]
    print('One month has passed, now here is my flock\n',n)
    print('Now my biggest sheep has size',max(n),"let's shear it")
    n[n.index(max(n))]=8
    print('After shearing, here is my flock \n',n)
n=[50+a for a in n]
print('One month has passed, now here is my flock\n',n)
t=0
for i in range(len(n)):
    t=t+n[i]
print('My flock has size in total: ',t)
print('I would get',t,'* 2 =',t*2,'$')
