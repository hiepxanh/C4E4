#1
##inventory = {
##'gold' : 500,
##'pouch' : ['flint', 'twine', 'gemstone'],
##'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
##}
##
##inventory["pocket"]=['seashell', 'strange berry', 'lint']
##inventory["backpack"].sort()
##
##inventory["backpack"].remove("dagger")
##inventory["gold"]=inventory["gold"]+50
##print(inventory)

#2
##price={"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}
##stock={"banana": 6,"apple": 0,"orange": 32,"pear": 15}
##def giatien(x):
##        for x,a in price.items():
##               return a
##def ton(y):
##        for y,b in stock.items():
##                return b
##
##
##print("in my store:\n")
##def bill(price,stock):
##    t= 0
##    for x,a in price.items():
##        for y,b in stock.items():
##            if x == y:
##                t = t + a*b
##    return t
##
##for x, a in price.items():
##    print (x,"\n price: ",a)
##    
##    for y, b in stock.items():
##        if x == y:
##            print("stock: ",b)
##
##print(" if we sold all of them we will earn totally is: ")
##print(bill(price,stock))


#3
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


def compute_bill():
    total=0
    for fruit,cost in prices.items():
        for fruit2,amount in stock.items():
            if fruit==fruit2:
                total=total+cost*amount
    print(total)
compute_bill()


print ("in Lulu store have:",stock)
print ("prices:", prices)

banana=int(input("banana:"))
while banana>6:
    print("Khong du de ban")
    banana=int(input("BananaAmount:"))

orange=int(input('orange:'))
while orange>32:
    print("Khong du de ban")
    orange=int(input('orange:'))

pear=int(input('pear:'))
while pear>15:
    print("Khong du de ban")
    pear=int(input('pear:'))

apple=int(input('aplle:'))
while apple>0:
    print("Khong du de ban")
    apple=int(input('apple:'))

print (str.format("if you buy this: apple {0}, pear {1}, orange {2}, banana{3}", apple,pear,orange,banana))
print ("You paid :", (apple * prices['apple']) + (pear * prices['pear'] + (orange * prices['orange']) + banana * prices['banana']))

if banana == 1:
    print ("you buyed banana")
if orange == 1:
    print ("you buyed orange")
if banana == 1 and orange == 1 :
    print("your total spend is : ", ((orange * prices['orange']) + banana * prices['banana']))

def remaining(banana,orange,pear,apple):
      
      for fruittype in stock:
            if fruittype=="banana":
                  stock['banana']=stock['banana']-apple
            if fruittype=="orange":
                  stock['orange']=stock['orange']-orange
            if fruittype=="pear":
                  stock['pear']=stock['pear']-pear
            if fruittype=="apple":
                  stock['apple']=stock['apple']-apple
      return(stock)
remaining(banana,orange,pear,apple)
print("Reamaining stuffs in Lulu's store is:",remaining(banana,orange,pear,apple))

