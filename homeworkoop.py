##1
class VendingMachine:
    drink = {'Coke':7,'Energy':10,'Water':5}
    def ChooseDrink(button):        
        if button == 1:
            drink = 'Coke'
        elif button == 2:
            drink = 'Energy'
        elif button == 3:
            drink = 'Water'
        return drink
        
    def getDrink(coin,drink):
        price = VendingMachine.drink[drink]
        while coin < price:
            coin = int(input('Please insert greater value: '))          
        if coin == price:
            print(str.format('Here is your {0}',drink))
        elif coin > price:
            change = coin - price
            print(str.format('Here is your {0} and {1}$ change',drink,change))

print('Please choose your drink from the list below:')
print(VendingMachine.drink)
print('Press 1 for Coke')
print('Press 2 for Energy')
print('Press 3 for Water')
b = int(input('I choose: '))
while b > 3 or b < 1:
    print('Drink unavailable')
    b = int(input('Please choose your drink: '))
c = int(input('Insert coin(s): '))
VendingMachine.getDrink(c,VendingMachine.ChooseDrink(b))

##2
class math_students:
    def __init__(self,name,classname):
        self.name = name
        self.classname = classname
    def greeting(self):
        print(str.format('I am {0} from class {1}, I can do simple calculations for you',self.name,self.classname))
    def calculate(self,x,y,sign):
        if sign == '+':
            return x + y
        elif sign == '-':
            return x - y
        elif sign == '*':
            return x * y
        elif sign == '/':
            return x / y
        elif sign == '**':
            return x**y
        elif sign == '//':
            return x // y
        elif sign == '%':
            return x % y
        else:
            print("I don't understand")

Hoa = math_students('Hoa','C4E4')
Hiep = math_students('Hiep','C4E2')

while True:
    who = input('Hoa or Hiep?')
    if who == 'Hoa':
        w = Hoa
        w.greeting()
        break
    if who == 'Hiep':
        w = Hiep
        w.greeting()
        break
    else:
        print('A.I not available!')
a,b,s = input('Input two numbers and one math sign, separated by space: ').split(' ')
a = int(a)
b = int(b)
print('Result = ',w.calculate(a,b,s))
