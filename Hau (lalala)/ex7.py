import pymongo
db_uri='mongodb://c4e:codethechange@ds021922.mlab.com:21922/cafeteria'
db=pymongo.MongoClient(db_uri).get_default_database()
connect_to_menu=db['menu']
d=db.collection_names()
for x in d:
    print(x)
connect_to_orders=db['orders']
# c=connect_to_orders.remove({})
# connect_to_orders.insert_many(
#     [{'customer': 'hiep', 'items': ['chips', 'black coffee']},
#      {'customer': 'huy', 'items': ['red tea']}])
# a=connect_to_menu.insert_many([
#     {'name':'black coffee',
#     'price': 2},
#     {'name':'red tea',
#     'price': 3},
#     {'name':'chips',
#      'price': 4}])
menu=connect_to_menu.find()
for x in menu:
    print(x)
# connect_to_orders.insert_one({
#     'customer':'lalala',
#     'items':['chips','red tea']
# })
order=connect_to_orders.find()
for x in order:
    print(x)
x=input('enter the name u want to compute bill:')
def billcompute(x):
    listt=connect_to_orders.find_one({'customer':x})
    total=0
    order = connect_to_orders.find()
    menu = connect_to_menu.find()
    for o in order:
        if x==o['customer']:
            for men in menu:
                for i in range(len(o['items'])):
                    if o['items'][i]==men['name']:
                        total=total+men['price']
    return total
print('you should pay:'+str(billcompute(x))+'$')