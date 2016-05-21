#Vending Machine
class VendingMachine:
    def __init__(self, drinkInfo):
        self.drinkInfo = drinkInfo

    def getDrink (self, coin, button):
        if button == 1:
            print("Here's your Coke and",coin - self.drinkInfo["Coke"],"VND")
        if button == 2:
            print("Here's your Energy and",coin - self.drinkInfo["Energy"],"VND")
        if button == 3:
            print("Here's your Water and",coin - self.drinkInfo["Water"],"VND")

coin = int(input("Input coin: "))
button = int(input("Input button (1-3): "))
Hoa = VendingMachine({"Coke":7,"Energy":10,"Water":5})
Hoa.getDrink(coin,button)
