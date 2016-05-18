class math_students:
    def __init__(self,name,classname):
        self.name = name
        self.classname = classname
    def greeting(self):
        print(str.format('Hi my name is {0} from class {1}, I can do simple calculations for you',self.name,self.classname))
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
            print('Operation not supported')

hoa = math_students('Hoa','C4E4')
hiep = math_students('Hiep','C4E2')
##hiep.greeting()
##print(hiep.calculate(6,2,'**'))
while True:
    who = input('We have 2 math students, Hoa and Hiep who can help you with your calculations. Which one would you choose to work with ? ')
    if who == 'Hoa':
        w = hoa
        w.greeting()
        print('')
        break
    elif who == 'Hiep':
        w = hiep
        w.greeting()
        print('')
        break
    else:
        print('Invalid name. Please choose between Hoa and Hiep only !')
        print('')
a,b,s = input('Now input two numbers and one math sign, separated with a space: ').split(' ')
a = int(a)
b = int(b)
print('Result = ',w.calculate(a,b,s))
