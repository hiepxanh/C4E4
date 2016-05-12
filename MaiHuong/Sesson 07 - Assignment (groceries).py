prices = {'banana' : 4,
          'apple' : 2,
          'orange' : 1.5,
          'pear' : 3
          }
stock = {'banana' : 6,
         'apple' : 0,
         'orange' : 32,
         'pear' : 15
         }
##total = 0
##for key1 in prices.items():
##    print(key1[0])
##    print('price: ', key1[1])
##    for key2 in stock.items():
##        if key1[0] == key2[0]:
##            print("stock: ", key2[1])
##            a = key1[1]* key2[1]
##            total += a
##print("If we sold out all of them, we can earn totally: ",total)
##
###### Exercise 3.1
##groceries = ['banana', 'orange', 'apple']
##prices = {'banana' : 4,
##          'apple' : 2,
##          'orange' : 1.5,
##          'pear' : 3
##          }
##stock = {'banana' : 6,
##         'apple' : 0,
##         'orange' : 32,
##         'pear' : 15
##         }
####def compute_bill(food):  
####    total = 0    
####    for i in range(3):
####        for x, y in prices.items():
####            if groceries[i] == x:           
####                total += y
####    return total
####print(compute_bill(groceries))
##
#### 3.2
groceries = ['banana', 'orange', 'apple']
prices = {'banana' : 4,
          'apple' : 2,
          'orange' : 1.5,
          'pear' : 3
          }
stock = {'banana' : 6,
         'apple' : 0,
         'orange' : 32,
         'pear' : 15
         }

    
print("In Lulu store have: ")
print(stock)
print("All the price is: ")
print(prices)
print("If you buy this: ")
print(groceries)

def compute_bill(food):
    total = 0

    for food in groceries:
        for food_stock in stock:
            if food_stock == food:                
                if stock[food] > 0:
                    total += prices[food]
                    print("You bought ", food)
                    stock[food_stock] = stock[food_stock] - 1
    print('Your total spend is: ', total)
    print('Remain stuff in Lulu store is: ', stock)


compute_bill(groceries)




    


    
