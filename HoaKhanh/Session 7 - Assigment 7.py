import pymongo
# 1,2,3,4
url = 'mongodb://c4e:codethechange@ds021922.mlab.com:21922/cafeteria'
db = pymongo.MongoClient(url).get_default_database()
menu = db['menu']
for item in menu.find():
    print(item['name'],':',item['price'])
orders = db['orders']
##orders.insert_one({'customer':'Hoa Khanh','items':['cookies','ice cream','red tea','chips']})
for order in orders.find():
    print(order['customer'],';',order['items'])

# 5 Compute bill
my_order = orders.find_one({'customer':'Hoa Khanh'})
print(my_order['customer'],':',my_order['items'])

total = 0
for item in my_order['items']:
    for food in menu.find():
        if item == food['name']:
            total += food['price']
print(total)


