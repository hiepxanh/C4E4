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
groceries = {}
def add_food(food, quan):
    groceries[food] = quan
    return groceries

n = ''
while n!= 'no':
    food = str(input("Nhap mat hang muon mua: "))
    quan = int(input("Nhap so luong: "))
    if food not in prices.keys():
            print("Hien chung toi khong co mat hang nay: ")
            n = str(input("Ban co muon mua them hang khong?: "))
    elif quan > stock[food]:
            print("Hien chung toi khong co du hang: ")
            n = str(input("Ban co muon mua them hang khong?: "))
    elif food in prices.keys() and quan <= stock[food]:
        add_food(food, quan)
        
        n = str(input("Ban co muon mua them hang khong?: "))

def compute_bill(food):
    total = 0
    for food in groceries:
        for food_stock in stock:
            if food_stock == food:
                if stock[food_stock] > 0:
                    total += prices[food] * groceries[food]                    
                    stock[food_stock] = stock[food_stock] - groceries[food]
    print("You bought ", groceries)
    return total
    return stock[food]

print('Your total spend is: ', compute_bill(groceries))
print('Remain stuff in Lulu store is: ', stock)




        
