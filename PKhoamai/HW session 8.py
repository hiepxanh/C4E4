class vendingMachine:
    def __init__(self):
        self.drinkinfo = {"Coke": 7, "Energy": 10, "Water": 5}
        self.buttonDict={"1":"Coke","2":"Energy","3":"Water"}

    def getdrink(self, coin, button):
        drink=self.buttonDict[str(button)]
        print("Here is your", drink)
        return coin - self.drinkinfo[drink]
        # if button ==1:
        #     print("Here is your Coke",coin-self.drinkinfo["Coke"],"VND")
        #     return coin - self.drinkinfo["Coke"]
        # if button ==2:
        #     print("Here is your Energy",coin-self.drinkinfo["Energy"],"VND")
        #     return coin - self.drinkinfo["Energy"]
        # if button ==3:
        #     print("Here is your water", coin - self.drinkinfo["water"], "VND")
        #     return coin - self.drinkinfo["water"]
PK =vendingMachine()
PK.getdrink(9,1)
class student:
    def __init__(self,name,age, ability):
        self.name = name
        self.age = -1
        self.ability = ability
    def calculation(self,n1, n2, sign):
        if sign =="+":
            result = int(n1)+int(n2)
            print ("student ",self.name," calculated for you, and the result is ", result)
        elif sign=="-":
            result = int(n1)-int(n2)
            print("student ", self.name, " calculated for you, and the result is ", result)
        elif sign=="*":
            result = int(n1)*int(n2)
            print("student ", self.name, " calculated for you, and the result is ", result)
        elif sign=="/":
            result = int(n1) / int(n2)
            print("student ", self.name, " calculated for you, and the result is ", result)
        else:
            print("Wrong sign")
PK=student("PK", 25,"calculation")
PK.calculation(8,25,"*")
