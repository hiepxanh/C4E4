file = open("ss5_data.txt")
luong=[]
for x in file:
    l = x.strip().split(" ")
    a = int(l[1])*int(l[2])
    luong.append(a)
print("Danh sach luong",luong)
