#EX1
inventory = {
'gold' : 500,
'pouch' : ['flint', 'twine', 'gemstone'],
'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory["pocket"]=['seashell', 'strange berry', 'lint']
inventory["backpack"].sort()

inventory["backpack"].remove("dagger")
inventory["gold"]=inventory["gold"]+50
print(inventory)
#EX2
price={"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}
stock={"banana": 6,"apple": 2,"orange": 32,"pear": 3}
def gia(x):
        for x,i in price.items():
               return i
def ton(y):
        for y,j in stock.items():
                return j

print("in my store:\n")
def compute_bill(price,stock):
        total =0
        for x,i in price.items():                
                for y,j in stock.items():
                        if x==y:
                                total = total+i*j
        return total
                       
for x,i in price.items():
                print(x,"\n price: ",i)
                
                for y,j in stock.items():
                        if x==y:
                                 print("\n stock: ",j)                             
        
print("\n if we sold all of them we will earn totally is: ")
print(compute_bill(price,stock))
#3:

groceries = ["banana","orange", "apple"]

