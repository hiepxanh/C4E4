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
