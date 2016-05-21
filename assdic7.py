##1
import pymongo
db_uri='mongodb://c4e:codethechange@ds021922.mlab.com:21922/cafeteria'
db=pymongo.MongoClient(db_uri).get_default_database()

##2
connect_to_menu=db['menu']
d=db.collection_names()
for x in d:
    print(x)
all_orders=db['orders']

##3
menu=all_orders.find()
for y in menu:
    if y in menu:
        print(y)

##4
order=all_orders.find()
for o in order:
    print(o)
all_orders.insert({"customer":"Nguyen Duc Minh",
              "items":"['black coffee']"})

##5
z=input('whose bill:')
def billcompute(z):
    listt=all_orders.find_one({'customer':z})
    total=0
    order = all_orders.find()
    menu = connect_to_menu.find()
    for orders in order:
        if z==orders['customer']:
            for menus in menu:
                for i in range(len(orders['items'])):
                    if orders['items'][i]==menus['name']:
                        total=total+menus['price']
    return total
print('to pay:'+str(billcompute(z))+'$')
