class vendingMachine:
    drinkinfo = {1: "Coke", 2: "Energy", 3: "Water"}
    price = {"Coke": 7, "Energy": 10, "Water": 5}

    def getdrink(coin, button):
        drinkinfo1 = vendingMachine.drinkinfo[button]
        return drinkinfo1
        price = vendingMachine.price[drinkinfo1]
        return price
        while coin<int(price):
            print("Please insert more valuable coin")
        if coin==int(price):
            print("Here is your ",drinkinfo1)
        elif coin>int(price):
            change=coin -int(price)
            print("Here is your ", drinkinfo1," and refund ", change)
print("Please choose you drink from below list:")
print(vendingMachine.drinkinfo)
b=int(input("I choose"))
while b>3 or b<1:
    print("Your drink is not available")
    b = int(input("Please choose your drink from 1 to 3"))
c=int(input("Insert coin"))
vendingMachine.getdrink(c,b)

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
