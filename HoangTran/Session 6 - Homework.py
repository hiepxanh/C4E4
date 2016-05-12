# # Bài 1:
#
# inventory = {
#     'gold': 500,
#     'pouch': ['flint', 'twine', 'gemstone'],
#     'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
# }
# inventory['pocket'] = ['seashell', 'strangeberry', 'lint']
# inventory['backpack'].sort()
# inventory['backpack'].remove('dagger')
# print(inventory['backpack'])
# inventory['gold']=inventory['gold']+50
# print(inventory['gold'])

# ----------------------------------------------------------------------------------------------------------------------

# #Bài 2:
# price = {"banana": 4,
#          "apple": 2,
#          "orange": 1.5,
#          "pear": 3
# }
#
# def stocking():
#     price[key]=[value, stock_input]
#     return key
#
# total=0
#
# for key, value in price.items():
#     print(key)
#     print("price: {0}".format(value))
#     stock_input = int(input("Input stock of {0}: ".format(key)))
#     total=total+(value*stock_input)
#     stocking()
#     print("stock: {0}".format(stock_input))
#     print()
#
# print("If we sold out all of them, we can earn totally: {0}".format(total))

# ----------------------------------------------------------------------------------------------------------------------

# Bài 3:

groceries=["banana","orange","apple"]

stock = {
"banana": 6,
"apple": 0,
"orange": 32,
"pear": 15
}

prices = {
"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
}

def compute_bill(foodlist):
    total = 0
    for food in foodlist:
        for keyP in prices.items():
            if food==keyP[0]:
                total=keyP[1]+total
    return total

groceries1=[]
groceries2=[]
groceries3=[]

for key_stock in stock.items():
    groceries1.append(key_stock)
print("LuLu Store has Stock: ", groceries1)

for key_prices in prices.items():
    groceries2.append(key_prices)
print("LuLu Store has Price: ", groceries2)

print("If you buy this: {0}".format(groceries))

for x in groceries:
    for y in stock.items():
        if x==y[0]:
            print("you will buy: ", x)

for food in groceries:
    for key_stock in stock.items():
        for key_prices in prices.items():
            if key_stock[0]==key_prices[0]==food:
                if key_stock!=0:
                    food={food: [key_prices[1], key_stock[1]]}
                    groceries3.append(food)
                    compute_bill(groceries)
print(compute_bill(groceries))
print (groceries3)

