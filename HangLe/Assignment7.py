#Ex1

import pymongo
db_uri = "mongodb://c4e:codethechange@ds021922.mlab.com:21922/cafeteria"
db=pymongo.MongoClient(db_uri).get_default_database()
# Ex2
menu_collection=db["menu"]
m=menu_collection.find()
for items in m:
    print(items['name'],':',items['price'])

#Ex3
order_collection=db["orders"]
m=order_collection.find()
for items in m:
    print(items)
    #print(items['customer'],':',items['items'])

#Ex4
order_collection.insert_one({"customer":"Hang","items":["black coffee",'red tea','chips']})
m=order_collection.find()
for items in m:
    print(items)
    #print(items['customer'],':',items['items'])

#Ex5
order = order_collection.find_one({"customer":"Hang"})
print(order["customer"],":",order['items'])
total=0
for x in order["items"]:
    for food in menu_collection.find():
        if x==food["name"]:
            total=total+food["price"]
print("your bill is: ",total)



