# Exercise 1
# inventory = {
#     'gold' : 500,
#     'pounch' : ['flint', 'twine','gemstone'],
#     'backpack' : ['xylophone','dagger', 'bedroll', 'bread loaf']
# }
# inventory['pocket'] = ['seashell', 'strange berry', 'lint']
# sorted(inventory)
# inventory['backpack'] = ['xylophone', 'bedroll', 'bread loaf']
# inventory['gold'] = 500, 50
# print(inventory)

# --------------------------------------------------------------------------------------------------
# Exercise 2
# total = 0
#
# stock = {
#     "banana": 6,
#     "apple": 0,
#     "orange": 32,
#     "pear": 15
# }
#
# prices = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }
#
# print("in my store:")
# print("")
#
#
# for key in prices:
#     print(key)
#     print("price:",prices[key])
#     print("stock:",stock[key])
#     total = total + prices[key]*stock[key]
#     print("")
#
# print("if we sold out all of them, we can earn totally is:",total)

# --------------------------------------------------------------------------------------------------
# Exercise 3
#Way 1: NO DEF
# food_list = ["banana","orange","apple"]
#
# stock = {
#     "banana": 6,
#     "apple": 0,
#     "orange": 32,
#     "pear": 15
# }
#
# prices = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }
#
# print("in store Lulu have:",stock)
# print("all the price is:",prices)
# print("if you buy this:",food_list)
#
# for food in food_list:
#     if food == "apple":
#         print("there isn't any apple left to buy")
#     else:
#         print("you buyed",food)
#
# total = 0
# for food in food_list:
#     if stock[food] > 0:
#         total = total + prices[food]
#     for food_stock in stock:
#         if food_stock == food:
#             if stock[food_stock] > 0:
#                 stock[food_stock] = stock[food_stock] - 1
#
# print('your total spend is',total)
# print("ramain stuff in Lulu store is:",stock)


#WAY 2: USE DEF
food_list = ["banana","orange","apple"]

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

print("in store Lulu have:",stock)
print("all the price is:",prices)
print("if you buy this:",food_list)

for food in food_list:
    if food == "apple":
        print("there isn't any apple left to buy")
    else:
        print("you buyed",food)

def compute_bill(x):
    total = x
    for food in food_list:
        if stock[food] > 0:
            total = total + prices[food]
        for food_stock in stock:
            if food_stock == food:
                if stock[food_stock] > 0:
                    stock[food_stock] = stock[food_stock] - 1
    return total

print('your total spend is',compute_bill(0))
print("ramain stuff in Lulu store is:",stock)