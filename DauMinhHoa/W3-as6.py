#Exercise 1
inventory = {
    'gold': 500,
    'pouch': ['flint', 'twince', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory['pocket']=['seashell', 'strange berry', 'lint'] #add key and value

inventory['backpack'].sort() #sort items in the list in 'backpack'

inventory['backpack'].remove('dagger') # remove 'dagger' from the list in 'backpack'

inventory['gold']= 500, 50 #add 50 to 500 in 'gold'

print(inventory)
#Exercise 2
prices = {
    'banana': 4,
    'apple': 2,
    'orange': 1.5,
    'pear': 3
}

stock = {
    'banana': 6,
    'apple': 0,
    'orange': 32,
    'pear': 15
}

print("in my store:")
print("")
for x in prices:
    print(x)
    print("price: ", int(prices[x]))
    print("stock: ", int(stock[x]))
    print("")
    
def profit(prices, stock):
    total=0
    for x,y in prices.items():
        for a,b in stock.items():
            if x==a:
                total=total + y*b
    return total

print("if we sold out all of them, we can earn:", profit(prices, stock))
