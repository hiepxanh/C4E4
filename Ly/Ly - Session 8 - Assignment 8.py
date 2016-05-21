#Vending Machine
class VendingMachine:
    def __init__(self, drinkInfo):
        self.drinkInfo = drinkInfo

    def getDrink (self, coin, button):
        if button == 1:
            if coin >= self.drinkInfo["Coke"]:
                print("You got Coke, and your change is:", coin - self.drinkInfo["Coke"], "VND")
            else:
                print("You need more money!")
        elif button == 2:
            if coin >= self.drinkInfo["Energy"]:
                print("You got Energy, and your change is:", coin - self.drinkInfo["Energy"], "VND")
            else:
                print("You need more money!")
        elif button == 3:
            if coin >= self.drinkInfo["Water"]:
                print("You got Water, and your change is:", coin - self.drinkInfo["Water"], "VND")
            else:
                print("You need more money!")

coin = int(input("Input coin: "))
button = int(input("Input button (1-3): "))
Ly = VendingMachine({"Coke":7,"Energy":10,"Water":5})
Ly.getDrink(coin,button)



#MathsStudent
class MathsStudent:
    def __init__ (self, name, className):
        self.name = name
        self.className = className

    def sayHello (x):
        print("Hello, my name is", x.name)
        print("My class: {0}" .format(x.className))

    def doCalculation(self, x, sign, y):
        if sign == "+":
            return x + y
        elif sign == "-":
            return x - y
        elif sign == "*":
            return x * y
        elif sign == "**":
            return x ** y
        elif sign == "/":
            return x / y
        elif sign == "//":
            return x // y
        elif sign == "%":
            return x % y
        else:
            print("Error")

Hoa = MathsStudent("Hoa", "C4E1")
Phuong = MathsStudent("Phuong", "C4E2")

while True:
    p = str(input("Hoa or Phuong: "))
    if p == "Hoa":
        p = Hoa
        p.sayHello()
        break
    elif p == "Phuong":
        p = Phuong
        p.sayHello()
        break
    else:
        print("Error")
        break

n,s,n1 = input("Input equation with space in between elements, e.g: 1 + 1: ").split(" ")
n = int(n)
n1 = int(n1)
result = p.doCalculation(n,s,n1)
print("Result = ", result)

