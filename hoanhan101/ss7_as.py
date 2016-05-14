import pymongo

# EX1
db_uri = "mongodb://c4e:codethechange@ds021922.mlab.com:21922/cafeteria"

db = pymongo.MongoClient(db_uri).get_default_database()

#EX2
menu_collection = db["menu"]
orders_collection = db["orders"]

# EX3
# all_menu = menu_collection.find()
# for x in all_menu:
#     print(x)
# all_menu = menu_collection.find()
# for x in all_menu:
#     print(x["name"], ":", x["price"])

# EX4
# orders_collection.insert_one({"customer":"hoanh","items":["white coffee","cookies"]})
# all_orders = orders_collection.find()
# for i in all_orders:
#     print(i["customer"],":",i["items"])

# EX5
all_orders = orders_collection.find_one({"customer":"hiep"})
print("Hiep's order:",all_orders["items"])
bill_chip = menu_collection.find_one({"name":"chips"})
bill_black_coffee = menu_collection.find_one({"name":"black coffee"})
print("Hiep has to pay:",bill_black_coffee["price"]+bill_chip["price"])
