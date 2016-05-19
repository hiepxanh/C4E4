class student:
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = -1
        self.hobby = hobby
    def calculate(self, no1, no2, sign):
        if sign == '+':
            result = int(no1) + int(no2)
            print('Student {0} calculated for you, and the result is {1}'.format(self.name,result))
        elif sign == '-':
            result = int(no1) - int(no2)
            print('Student {0} calculated for you, and the result is {1}'.format(self.name, result))
        elif sign == '*':
            result = int(no1) * int(no2)
            print('Student {0} calculated for you, and the result is {1}'.format(self.name, result))
        elif sign == '/':
            result = int(no1) / int(no2)
            print('Student {0} calculated for you, and the result is {1}'.format(self.name, result))
        else:
            print('Wrong sign.')

giang = student('Giang',19,'reading')
giang.calculate(10,14,'-')