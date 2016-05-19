class MathsStudent:
    def __init__(self, n, c):
        self.name = n
        self.classname = c
    def calculation(self, x, y, sign):
        print("Hello, my name is ", self.name)
        print("I take class ", self.classname)
        print('I can do calculation:')
        if sign == "+":
            print(str.format("{0} + {1} = {2}", x, y, sum(x, y)))
        elif sign == "-":
            print(str.format("{0} - {1} = {2}", x, y, x - y))
        elif sign == "*":
            print(str.format("{0} * {1} = {2}", x, y, x*y))
        elif sign == "/":
            print(str.format("{0} / {1} = {2}", x, y, x/y))
        elif sign == "**":
            print(str.format("{0} ** {1} = {2}", x, y, x**y))
        elif sign == "//":
            print(str.format("{0} // {1} = {2}", x, y, x // y))

Hiep = MathsStudent('Hiep', 'C4E4')
Hoa = MathsStudent('Hoa', 'C4E2')
while True:
    n = input("Hoa or Hiep?: ")
    x, y, sign = input('Enter two numbers and 1 math sign: ').split(" ")
    x = int(x)
    y = int(y)
    if n == 'Hoa':
        n = Hoa
        n.calculation(x, y, sign)
    elif n == "Hiep":
        n = Hiep
        n.calculation(x, y, sign)







# x, y, sign = input('Enter two numbers and 1 math sign').split(" ")
# hoa.calculation(x, y, sign)