import pymongo
db_uri="mongodb://c4e:codethechange@ds021922.mlab.com:21922/cafeteria"
db=pymongo.MongoClient(db_uri).get_default_database()
menu_collection=db["menu"]
m=menu_collection.find()
for item in m:
    print(item)

order_collection=db["orders"]
n=order_collection.find()
for order in n:
    if "customer" in order:
        print(order["customer"],order)

##order_collection.insert_one({"customer":"PK","items":["chips"]})
order_collection=db["orders"]
n=order_collection.find()
for order in n:
    if "customer" in order:
        print(order["customer"],order)
order = order_collection.find_one({"customer":"PK"})
print(order["customer"],"'s order",order)
total=0
for x in order["items"]:
    for food in menu_collection.find():
        if x==food["name"]:
            total=total+food["price"]
print("your bill is: ",total)




