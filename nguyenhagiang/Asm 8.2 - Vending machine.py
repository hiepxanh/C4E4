class vending_machine:
    def __init__(self):
        drinkinfo = [{'name':'Coke','price':7,'button':1},{'name':'Energy','price':10,'button':2},{'name':'Water','price':5,'button':3}]
        self.drinkinfo = drinkinfo

    def getdrink(self, coin, button):
        for item in self.drinkinfo:
            if button == item['button']:
                if coin < item['price']:
                    print('You are buying', item['name'])
                    print("You don't have enough money to buy ", item['name'])
                elif coin == item['price']:
                    print('You are buying', item['name'])
                    print('Your money is enough for', item['name'])
                else:
                    print('You are buying ', item['name'])
                    change = coin - item['price']
                    print('Please take your change', change,'coin')
                print('Enjoy your', item['name'])

x = vending_machine()
x.getdrink(15, 1)
print()
x.getdrink(10,2)
print()
x.getdrink(3,3)