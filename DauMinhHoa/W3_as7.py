import pymongo

# EX1
db_uri = "mongodb://c4e:codethechange@ds021922.mlab.com:21922/cafeteria"

db = pymongo.MongoClient(db_uri).get_default_database()

#EX2
menu_collection = db["menu"]
orders_collection = db["orders"]

# EX3

all_menu = menu_collection.find()
# for x in all_menu:
#     print(x["name"], ":", x["price"])

# Ex4: Place order
order_collection.insert_one(
    {
        'hiep':['black coffee', 'chips']
    }
)



order = order_collection.find()
for y in o:
    print(y)

# EX5
you = input("Whose bill:")

customer_order = orders_collection.find_one({"customer":you})
print(u,"order: ",customer_order["items"])

total = 0
for menu in all_menu:
    for order in customer_order["items"]:
        if order == menu["name"]:
            total = total + menu["price"]
print(you,"has to pay:",total)
