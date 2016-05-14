import pymongo
db_uri = "mongodb://c4e:codethechange@ds021922.mlab.com:21922/cafeteria"
db = pymongo.MongoClient(db_uri).get_default_database()
## connect to the database

menu_collection = db['menu']
name_collection = db.collection_names()
orders_collection = db['orders']
# for name in name_collection:
#     print(name)

menu_find = menu_collection.find()
# for i in menu_find:
#     print(i)
## print all item in collection "menu"

# for m in menu_find:
#     print(m['name'], ":", m['price'])
## print all item in collection "menu" as: <item> : <price>

order_find = orders_collection.find()
# for ord in order_find:
#     print(ord['customer'], ':', ord['items'])
## print out all item in collection 'orders' as required

# orders_collection.insert_one(
#     {'customer' : 'Huong',
#      'items' : ['bread', 'chips', 'black coffee']}
# )
## use insert_one to insert my order

# for ord in order_find:
#     print(ord['customer'], ":", ord['items'])
## print out all orders again
#
order_Huong = orders_collection.find({'customer' : 'Huong'}
)
for i in order_Huong:
    print("Huong's order: ", i['items'])
    bill_total = 0
    for each_item in i['items']:
        price_find = menu_collection.find()
        for price in price_find:
            if each_item == price['name']:
                print("You order ", each_item, ":", price['price'])
                bill_total += price['price']
print("All you have to pay: ", bill_total)
## print out my order and compute the bill I have to pay










