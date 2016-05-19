# MATH STUDENT
# class student:
#     def __init__(self, name, age, hobby):
#         self.name = name
#         self.age = -1
#         self.hobby = hobby
#     def calculate(self, no1, sign, no2):
#         if sign == "+":
#             result = int(no1)+int(no2)
#             print("Student {0} have calculated for you, the result is {1}".format(self.name, result))
#         elif sign == "-":
#             result = int(no1) - int(no2)
#             print("Student {0} have calculated for you, the result is {1}".format(self.name, result))
#         elif sign == "*":
#             result = int(no1) * int(no2)
#             print("Student {0} have calculated for you, the result is {1}".format(self.name, result))
#         elif sign == "/":
#             result = int(no1) / int(no2)
#             print("Student {0} have calculated for you, the result is {1}".format(self.name, result))
#         else:
#             print("Wrong sign")
#
# hoang = student("Hoang", 18, "fishing")
# hoang.calculate(5, "+", 5)


# -------------------------------------------------------------------------------------------------------------


#VENDING MACHINE - Cach 1
# class vending_machine:
#     def __init__(self, coin, button):
#             self.coin = coin
#             self.button = button
#
#     def getDrink(self):
#         drinkinfo = [{"name": "Coke", "price": 7, "button": 1}, {"name": "Energy", "price": 10, "button": 2},
#                      {"name": "Water", "price": 5, "button": 3}]
#         for item in drinkinfo:
#             if self.button == item['button']:
#                 print(item['name'])
#                 change = self.coin - item['price']
#                 print (change)
#
# hoang = vending_machine(15, 2)
# hoang.getDrink()

# -------------------------------------------------------------------------------------------------------------
#

# VENDING MACHINE - Cach 2
class vending_machine:
    def __init__(self):
        drinkinfo = [{"name": "Coke", "price": 7, "button": 1}, {"name": "Energy", "price": 10, "button": 2},
                     {"name": "Water", "price": 5, "button": 3}]
        self.drinkinfo = drinkinfo

    def getDrink(self, coin, button):
        for item in self.drinkinfo:
            if button == item['button']:
                if coin < item['price']:
                    print("You are buying", item['name'])
                    print("Not enough coin to buy", item['name'])
                else:
                    print("You are buying", item['name'])
                    change = coin - item['price']
                    print ("Here is your change ", change)

hoang = vending_machine()
hoang.getDrink(6, 1)


