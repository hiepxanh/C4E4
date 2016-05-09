##for number in 5,7,11,13:
## print(number)
##print("total:",5+7+11+13)
##
##
##for i in range(1001):
##    print("Anh Yeu Em !!!")
##print("Anh Yeu Em 1001 lan roi nhe")

##l = ["Chua bao gio","De em roi xa","Tam su voi nguoi la"]
##print("My playlist is:")
##for i in l:
##    print(l.index(i),":",i)

##import time
##import webbrowser
##
##l = ["https://www.youtube.com","https://www.google.com","https://www.tinhte.vn"]
##
##def open_browser(t,u):
##    time.sleep(t)
##    webbrowser.open(u)
##
##x = input("What browser: ")
##if x == "Youtube":
##    open_browser(5,l[0])
##if x == "Google":
##    open_browser(5,l[1])
##if x == "Tinhte":
##    open_browser(5,l[2])

##example_dict = {"Column 1":[1,2,3],"Column 2": [4,5,6], "Column 3": [7,8,9]}
##sheet = pyexcel.get_sheet(adict=example_dict)
##sheet.save_as("output.xlsx")

##records=pe.get_records(file_name="hoanhan.xlsx")
##for record in records:
##    print("%s is aged at %d" % (record["Name"],record["Age"]))

##ten_lop = {"Họ tên":["Trần Quang Hiệp","Nguyễn Quang Huy","Nguyễn Quang Huy","Nguyễn Quang Huy","Nguyễn Hà San","Nguyễn Hà San"],"Lớp": ["C4E3","C4E1","C4E2","C4E3","Android1","iOS1"]}
##sheet = pyexcel.get_sheet(adict=ten_lop)
##sheet.save_as("ten_lop.xlsx")

from turtle import*
##def draw(x):
##    for i in range(x):
##        forward(100)
##        left(360/x)
##
##d = input("Which shape: ")
##if d=="tamgiac":
##    draw(3)
##if d=="tugiac":
##    draw(4)
##if d=="ngugiac":
##    draw(5)

##def old_friend(x):
##    for i in range(x):
##        x = x + 1
##        penup()
##        forward(x)
##        pendown()
##        forward(x)
##old_friend(10)

def draw(x):
    for i in range(x):
        forward(100)
        left(360/x)

for i in range(6):
    forward(100)
    right(60)
    draw(6)

