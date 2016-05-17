#1
import pymongo
db_uri='mongodb://c4e:codethechange@ds021922.mlab.com:21922/cafeteria'
db=pymongo.MongoClient(db_uri).get_default_database()
connect_to_menu=db['menu']
#2
menu=connect_to_menu.find()
for x in menu:
    print(x)
#3,4
connect_to_orders=db['orders']
connect_to_orders.insert([{'customer': 'hiep', 'items': ['chips', 'black coffee']},
      {'customer': 'huy', 'items': ['red tea']}])
order=connect_to_orders.find()
for x in order:
    print(x)
#5
x=input("Enter the name you want to compute bill :")
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