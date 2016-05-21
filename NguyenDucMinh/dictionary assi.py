##1
inventory = {
      'gold': 500,
      'pouch': ['flint', 'twine', 'gemstone'],
      'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
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
     "banana": 4,
     "apple": 2,
     "orange": 1.5,
     "pear": 3
 }
stock = {
     "banana": 6,
     "apple": 4,
     "orange": 32,
     "pear": 15
 }
total=0
def in_my_store(prices,stock):
     for x,y in prices.items():
         print('\n'+x)
         print('price:'+str(y))
         for z,w in stock.items():
             if z==x:
                 print('stock:'+str(w))
    
def profit(prices,stock):
     total=0
     for x,y in prices.items():
         for z,w in stock.items():
             if x==z:
               total=total+y*w
     return total
print ('In my store:')
print (in_my_store(prices,stock))
print (profit(prices,stock))

##3
stock2={
    'banana':6,
    'apple':0,
    'orange':32,
    'pear':15}
prices2={
    'banana':4,
    'apple':2,
    'orange':1.5,
    'pear':3}
foodlist=[stock2,prices2]

def compute_bill(food):
    total=0
    for fruit,cost in prices2.items():
        for fruit2,amount in stock2.items():
            if fruit==fruit2:
                total=total+cost*amount
    print(total)
compute_bill(foodlist)

##3.5
print ("in Lulu store:",stock2)
print ("prices:", prices2)

banana_purchase=int(input("BananaAmount:"))
while banana_purchase>6:
    print("Insufficent Stock")
    banana_purchase=int(input("BananaAmount:"))

orange_purchase=int(input('OrangeAmount:'))
while orange_purchase>32:
    print("Insufficient Stock")
    orange_purchase=int(input('OrangeAmount:'))

pear_purchase=int(input('PearAmount:'))
while pear_purchase>15:
    print("Insufficient Stock")
    pear_purchase=int(input('PearAmount:'))

print (str.format("You bought:{0} banana(s), {1} orange(s),{2} pear(s)",banana_purchase,orange_purchase,pear_purchase))
print ("You paid:",banana_purchase*4+orange_purchase*1.5+pear_purchase*3)

def remaining_stock(a,b,c):
      
      for fruittype in stock2:
            if fruittype=="banana":
                  stock2['banana']=stock2['banana']-a
            if fruittype=="orange":
                  stock2['orange']=stock2['orange']-b
            if fruittype=="pear":
                  stock2['pear']=stock2['pear']-c
      return(stock2)
      
print("Reamaining stuffs in Lulu's store is:",remaining_stock(banana_purchase,orange_purchase,pear_purchase))





