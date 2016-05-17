##1
inventory = {
    "gold" :500,
    "pouch":['plint','twine','gemstore'],
    'backpack':['xylophone','dagger','bedroll','bread loaf']
    }
pocket=['seashell','strange berry','lint']
for x,y in inventory.items():
    if x=='backpack':
        y.sort()
        y.remove('dagger')
    elif x=='gold':
        inventory['gold']=y+50
print(inventory)
##2
prices={
    "banana":4,
    "apple":2,
    "orange":1.5,
    "pear":3
    }
stock={
    "orange":32,
    "pear":15,
    "banana":6,
    "apple":0
    }
def in_store(prices,stock):
    for x,y in prices.items():
        print("\n" + x +" :")
        print('prices :'+str(y))
        for z,w in stock.items():
            if z==x:
                print("stock :"+ str(w))
in_store(prices,stock)
def in_total(prices,stock):
    total=0
    for x,y in prices.items():
        for z,w in stock.items():
            if x==z:
                total=total+y*w
    return total
print("if we sold out all of them, we can earn totally :",in_total(prices,stock))
