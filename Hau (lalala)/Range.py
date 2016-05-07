def combi(n):
    if n==0:
        return 1
    else:
        return combi(n-1)*n
a=input('n: ')
a=int(a)
s1=0
s2=0
for x in range (1,a+1,1):
    s1=s1+1/x
    s2=s2+1/combi(x)
print(round(s1,2))
print(round(s2,2))
