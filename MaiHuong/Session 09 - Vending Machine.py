
##class VendingMachine:
##    def __init__(self, drinkInfo ):
##        self.drinkInfo = drinkInfo
##
##    def getDrink(self, coin, button):
##        if button == 1:
##            drink = 'Coke'
##        elif button == 2:
##            drink = 'Energy'
##        elif button == 3:
##            drink = 'Water'
##        print('You choose',drink)
##        for item in self.drinkInfo.items():
##            if drink == item[0]:
##                print('Please, get your ', item[0], 'and receive excessive change: ', coin - item[1])
##huong = VendingMachine({'Coke': 7,
##                          'Energy' : 10,
##                           'Water' : 5})
##
##huong.getDrink(12, 1)



class VendingMachine:
    def __init__(self, drinkInfo ):
        self.drinkInfo = drinkInfo

    def Drink(button):
        if button == 1:
            drink = 'Coke'
        elif button == 2:
            drink = 'Energy'
        elif button == 3:
            drink = 'Water'
        return drink

    def getDrink(self, coin, drink):
        price = self.drinkInfo[drink]

        print('You choose: ', drink)
        print('Please, get your ', drink, 'and your change: ', coin - price)
drinkInfo = {'Coke': 7,
                          'Energy' : 10,
                           'Water' : 5}

print("Here's menu:")
index = 1
for item in drinkInfo.items():
    print(str.format('{0}. {1} price: {2}', index, item[0], item[1]))
    index += 1

while True:
    coin = int(input('Enter your coin: '))
    button = int(input('Enter your choice: '))

    huong = VendingMachine(drinkInfo)
    huong.getDrink(coin, VendingMachine.Drink(button))





