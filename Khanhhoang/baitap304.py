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
for i in n:
    if(i>t):
        t=i
    else:
        t=t
print('Now my biggest sheep has size',t,"let'shear it")
