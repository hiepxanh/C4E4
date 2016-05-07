s = [5,7,300,50,90,24,50,75]
print ("Hi I'm Khang and my my sheeps sizes are")
print (s)
print ("Now my largest sheep has size", max(s))
print ("Let's shear it")
s.remove(max(s))
s.insert(1,8)
print ("After shearing, here is my flock")
print (s)
a =[x+50 for x in s]
print ("1 month has passed, here is my flock")
print (a)

print ("Now my largest sheep has size", max(a))
print ("Let's shear it")
a.remove(max(a))
a.insert(1,8)
print ("After shearing, here is my flock")
print (a)
b =[x+50 for x in a]
print ("2 months has passed, here is my flock")
print (b)

print ("Now my largest sheep has size", max(b))
print ("Let's shear it")
b.remove(max(b))
b.insert(1,8)
print ("After shearing, here is my flock")
print (b)
c =[x+50 for x in b]
print ("3 months has passed, here is my flock")
print (c)

print ("Now my largest sheep has size", max(c))
print ("Let's shear it")
c.remove(max(c))
c.insert(1,8)
print ("After shearing, here is my flock")
print (c)
d =[x+50 for x in c]
print ("4 months has passed, here is my flock")
print (d)


