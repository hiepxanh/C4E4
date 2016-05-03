
# Exercise 2: flock of sheeps
from turtle import *
sizes = [5, 7, 300, 90, 24, 50, 75] ## flock sizes
print("Hello, my name is Hiep and these are my sheep sizes ", sizes)
n = int(input("Nhap thang can thu hoach: "))   
for t in range(1, n+1):
    print("MONTH ", t, ":")
    sizes = [50 + size for size in sizes]
    print("One month has passed and here is my flock", sizes)
    if t == n:
        print("Flock has sizes in total: ", sum(sizes))
        print(str.format("I would has {0} * 2$ = {1}", sum(sizes), sum(sizes) * 2))
    else:
        print("Now my biggest sheep has size", max(sizes), "let's sheer it")
        max_size_index = sizes.index(max(sizes))
        sizes[max_size_index] = 8
        print("After shearing, here is my flock", sizes)

mainloop()
    
