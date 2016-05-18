# class Car:
#     manufacturer = ""
#     year = -1
#     def print(self):
#         print("Manufacturer:" + str(self.manufacturer))
#         print("Year:" + str(self.year))
#
# c = Car()
# c.manufacturer = "Toyota"
# c.year = 2014
# c.print()

# class person:
#     def __init__(self, n,a,address):
#         self.name = n
#         self.age = a
#         self.address = address
#     # name = ""
#     # age = -1
#     # address = ""
#     def sayHello(self):
#         print("Hello, my name is ", self.name)
#         print("I'm {0} year old".format(self.age))
#         print("My address : {0}".format(self.address))
# hoanh = person("Hoanh", 19, "Tran Khat Tran, Ha Noi")
# hoanh.name = "Hoanh"
# hoanh.age = 19
# hoanh.address = "Tran Khat Tran, Ha Noi"
# hoanh.sayHello()
####################                            HW 8
# class VendingMachine:
#     def __init__(self, drink ):
#         self.drink = drink
#     def get_drink(self,coin, button):
#         if button == 1:
#             print ("Bạn chọn Coca và số tiền dư là :", coin - self.drink["Coke"] ,"VND")
#         if button == 2:
#             print ("Bạn chọn Nước Tăng Lực và số tiền dư là :", coin - self.drink["Energy"],"VND")
#         if button == 3:
#             print ("Bạn chọn Nước và số tiền dư là :", coin - self.drink["Water"], "VND")
#
# tu = VendingMachine({"Coke" : 7, "Energy" : 10 , "Water" : 5})
# coin = int(input("My coin :"))
# button = int(input("Choose button (1-3) :"))
# tu.get_drink(coin,button)

class MathsStudent:
    def __init__(self,name,classN):
        self.name = name
        self.classN = classN
    def calculate(self,Calc,a,b):
        print("My name is",self.name,"of",self.classN)
        if Calc == "+":
            print("Result :",a,"+",b,"=",a+b)
        if Calc == "-":
            print("Result :",a,"-",b,"=",a-b)
        if Calc == "*":
            print("Result :",a,"*",b,"=",a*b)
        if Calc == "/":
            print("Result :",a,"/",b,"=",a/b)

hoa = MathsStudent("Hoa","C4E4")
hoa.calculate("+",3,2)
hoa.calculate("-",4,2)
hiep = MathsStudent("Hiep","C4E2")
hiep.calculate("*",1,2)
hiep.calculate("/",2,1)