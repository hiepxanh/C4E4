##from linecache import*
##x=open('filex.txt')
##a=[]
##c=[]
##a=x.readlines()
##for i in range(len(a)):
##    c.append(a[i].split(' '))
##d=[]
##for i in range (len(c)):
##    d.append(int(c[i][1])*int(c[i][2]))
##    print(c[i][0]+' get '+ str(d[i])+' this month')
##
##import webbrowser
##import time
##from turtle import*
##def getinternet(i):
##    lit=['https://www.facebook.com','https://www.youtube.com/','http://www.tutorialspoint.com/python/time_sleep.htm']
##    if i=='1':
##        webbrowser.open(lit[0])
##    elif i=='2':
##        webbrowser.open(lit[1])
##    else:
##        webbrowser.open(lit[2])
##i=input('number plz:')
##getinternet(i)
import pyexcel as pe
import pyexcel.ext.xls
record=pe.get_records(file_name='xxx.xls')
for record in records:
    print("%s is aged at %d" %(record['Name'],record['Age']))
