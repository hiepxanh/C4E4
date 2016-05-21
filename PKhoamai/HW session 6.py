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
stock={"banana": 6,"apple": 0,"orange": 32,"pear": 3}
def gia(x):
        for x,i in price.items():
               return i
def ton(y):
        for y,j in stock.items():
                return j

print("in my store:\n")
def compute_bill(x):
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
print(compute_bill(x))
#3:
price={"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}
stock={"banana": 6,"apple": 0,"orange": 32,"pear": 3}
groceries = ["banana","orange", "apple"]
print ('in Lulu store have: ',stock)
print ('all the price is: ',price)
print( 'if you buy this: ',groceries)

def bill(food):
        total = 0
        for i in food:
                if i in stock and stock[i]>1:            
                    print('you bought',i)
                    total += price[i]
                    stock[i] = stock[i] - 1
                else:
                        print(i, ": your food you chose is not available")
        print('your total expense is:',total)
        print('remaining stuff in Lulu store is:',stock)
        return total
        return stock

print("your total spend is: ", total)
print("remain stuff in Lulu store is: ", stock)
bill(groceries)


