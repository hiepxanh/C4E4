# class MathsStudent:
#     def __init__(self,name,className):
#         self.name = name
#         self.className = className
#     def calculate(self,doCalculation,a,b):
#         print("My name is",self.name,"of",self.className)
#         if doCalculation == "Addition":
#             print("Result of addition:",a,"+",b,"=",a+b)
#         if doCalculation == "Substraction":
#             print("Result of substraction:",a,"-",b,"=",a-b)
#         if doCalculation == "Mutiplication":
#             print("Result of mutiplication:",a,"*",b,"=",a*b)
#         if doCalculation == "Division":
#             print("Result of division:",a,"/",b,"=",a/b)
#
# hoa = MathsStudent("Hoa","C4E4")
# hoa.calculate("Addition",1,2)
# hoa.calculate("Substraction",2,1)
# print("------------------------------------------------------")
# hiep = MathsStudent("Hiep","C4E2")
# hiep.calculate("Mutiplication",1,2)
# hiep.calculate("Division",2,1)

class VendingMachine:
    def __init__(self,drinkInfo):
        self.drinkInfo = drinkInfo
    def getDrink(self,coin,button):
        if button == 1:
            print("Here's your Coke and",coin - self.drinkInfo["Coke"],"VND")
        if button == 2:
            print("Here's your Energy and",coin - self.drinkInfo["Energy"],"VND")
        if button == 3:
            print("Here's your Water and",coin - self.drinkInfo["Water"],"VND")

hoanh = VendingMachine({"Coke":7, "Energy":10,"Water":5})
hoanh.getDrink(9,1)
hoanh.getDrink(10,2)
hoanh.getDrink(11,3)