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

# EX4
# orders_collection.insert_one({"customer":"hoanh","items":["chips","red tea"]})
all_orders = orders_collection.find()
# for i in all_orders:
#     print(i["customer"],":",i["items"])

# EX5
u = input("Whose bill:")

customer_order = orders_collection.find_one({"customer":u})
print(u,"order: ",customer_order["items"])

total = 0
for menu in all_menu:
    for order in customer_order["items"]:
        # for menu in all_menu:
        if order == menu["name"]:
            total = total + menu["price"]
print(u,"has to pay:",total)



