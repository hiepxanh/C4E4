def stoa(s):
    l=[]
    for i in s:
        l.append(ord(i)+2)
    return (l)
def atos(l):
    string=[]
    for i in l:
        string.append(chr(i))
    return (string)
l=stoa("Khanh Hoang")
print(atos(l))
