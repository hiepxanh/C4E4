import pymongo

#Excercise 1: Connect to database
db_uri = "mongodb://c4e:codethechange@ds021922.mlab.com:21922/cafeteria"

db=pymongo.MongoClient(db_uri).get_default_database()



#Excercise 2 & 3: load menu, load orders
menu_collection = db["menu"]
order_collection = db["orders"]
price_collection = db["price"]

m = menu_collection.find()
for x in m:
    print(x)



#Exercise 4: insert order
order_collection.insert_one(
    {
        'Ly':['black coffee','green tea', 'chips']
    }
)

o = order_collection.find()
for x1 in o:
    print(x1)



#Exercise 5: compute bill
bill = input(str("Who to pay: "))

customer_order = order_collection.find_one({"customer":bill})
all_menu = menu_collection.find()

def compute_bill(bill):
    total = 0
    for menu in all_menu:
        for order in customer_order["items"]:
            if order == menu["name"]:
                total = total + menu["price"]
    return total

print(bill,"ordered: ", customer_order["items"])
print(bill, "to pay :", str(compute_bill(bill)))
