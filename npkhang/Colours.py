L = ["Blue","Red","Purple","Yellow","Green"]
print (L)

print (L[0])
print (L[1])
print (L[2])
print (L[3])
print (L[4])
for i in range (100):
    
    color = input("What is your favourite color? ")

    if color in L:
        print(color + " is at index ")
        print(L.index(color))
    else:
        print("Your colour is not in my list")
