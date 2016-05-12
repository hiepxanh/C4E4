# Ex 1
inventory = {'gold': 500, 'pouch': ['flint','twine','gemstone'],'backpack':['xylophone','dagger','bedroll','breadloaf']}
inventory['pocket']=['seashell','strang berry','lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] += 50
# Ex 2
prices = {'banana': 4, 'apple': 2, 'orange': 1.5,'pear': 3}
stock = {'banana': 10, 'apple': 4, 'orange': 3,'pear': 6}
total = 0
for x in prices:
    print(x)
    print('price:',prices[x])
    print('stock:',stock[x]) 
    total += prices[x]*stock[x]
print('Total revenue:',total)
# Ex 3
groceries = ['banana','orange','apple']
stock = {'banana':6,'apple':0,'orange': 32,'pear':15}
prices = {'banana':4,'apple':2,'orange':1.5,'pear':3}
def compute_bill(foodlist):
    total = 0
    for i in foodlist:
        if i not in stock or stock[i] <= 0: pass
        else:            
            print('you bought',i)
            total += prices[i]
            stock[i] = stock[i] - 1
    print('your total expense is:',total)
    print('remaining stuff in Lulu store is:',stock)
    return total
    return stock
print('Food in Lulu store',stock)
print('All the prices are:',prices)
print('If you buy:',groceries)
compute_bill(groceries)
