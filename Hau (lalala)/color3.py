mycolor=['red','blue','green','black','white','yellow','brown']
a=False
count=0
v=input('What is your favorite color?')
for x in mycolor:
    if x==v:
        a=True
        break
    count=count+1
if a==True:
    print('There is '+v+' in the list at '+str(count))
else:
    print('none of these is your color')
num=input('number?')
num=int(num)
print('at '+str(num)+':'+mycolor[num])
print(mycolor)
for c in mycolor:
    print(c)
