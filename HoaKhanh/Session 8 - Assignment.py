class VendingMachine:
    drinkInfo = {'Coke':7,'Energy':10,'Water':5}
    def checkDrink(button):        
        if button == 1:
            drink = 'Coke'
        elif button == 2:
            drink = 'Energy'
        elif button == 3:
            drink = 'Water'
        return drink
        
    def getDrink(coin,drink):
        price = VendingMachine.drinkInfo[drink]
        while coin < price:
            coin = int(input('Please insert a coin with larger value: '))          
        if coin == price:
            print(str.format('Please get your {0} !',drink))
        elif coin > price:
            change = coin - price
            print(str.format('Please get your {0} and {1}$ change',drink,change))

print('Please choose your drink from the list below:')
print(VendingMachine.drinkInfo)
print('Press 1 for Coke')
print('Press 2 for Energy')
print('Press 3 for Water')
b = int(input('I choose: '))
while b > 3 or b < 1:
    print('Your chosen drink is not available !')
    b = int(input('Please choose your drink again: '))
c = int(input('Insert your coin: '))
VendingMachine.getDrink(c,VendingMachine.checkDrink(b))
