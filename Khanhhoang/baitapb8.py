#1
class MathsStudent:
    name = " "
    className = " "
    x = -1
    y = -1
    Cal = " "
    def  __init__(self,name,className):
        self.name=name
        self.className=className
    def greeting(self):
        print(str.format("I'm {0} from class {1}",self.name,self.className))
    def doCal(self,Cal,x,y):
        if Cal == "+":
            return (x+y)
        elif Cal == "-":
            return (x -y)
        elif Cal == "*":
            return (x*y)
        elif Cal == "/":
            return (x/y)
        else:
            print("Error")
hoa = MathsStudent("Hoa", "C4E")
phuong = MathsStudent("Phuong","C4E")
hoa.greeting()
phuong.greeting()
Cal,x,y = input("Enter number and Calculate").split(' ')
x = int(x)
y =int(y)
print("Result",hoa.doCal(Cal,x,y))
# 2
class VendingMachine:
    drink = {'Coke': 7, 'Energy': 10, 'Water': 5}

    def ChooseDrink(button):
        if button == 1:
            drink = 'Coke'
        elif button == 2:
            drink = 'Energy'
        elif button == 3:
            drink = 'Water'
        return drink

    def getDrink(coin, drink):
        price = VendingMachine.drink[drink]
        while coin < price:
            coin = int(input('Please insert greater value: '))
        if coin == price:
            print(str.format('Here is your', drink))
        elif coin > price:
            change = coin - price
            print(str.format('Here is your {0} and {1}$ change', drink, change))

b = int(input('I choose: '))
while b > 3 or b < 1:
    print('Error')
    b = int(input('Please choose your drink: '))
c = int(input('Insert coin(s): '))
VendingMachine.getDrink(c, VendingMachine.ChooseDrink(b))