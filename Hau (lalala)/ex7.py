import pymongo
db_uri='mongodb://c4e:codethechange@ds021922.mlab.com:21922/cafeteria'
db=pymongo.MongoClient(db_uri).get_default_database()
# connect_to_menu=db['menu']
# print(db.collection_names())
# for x in d:
#     print(x)
# connect_to_orders=db['orders']
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
# menu=connect_to_menu.find()
# for x in menu:
#     print(x)
# connect_to_orders.insert_one({
#     'customer':'lalala',
#     'items':['chips','red tea']
# })
# order=connect_to_orders.find()
# for x in order:
#     print(x)
# x=input('enter the name u want to compute bill:')
# def billcompute(x):
#     listt=connect_to_orders.find_one({'customer':x})
#     total=0
#     order = connect_to_orders.find()
#     menu = connect_to_menu.find()
#     for o in order:
#         if x==o['customer']:
#             for men in menu:
#                 for i in range(len(o['items'])):
#                     if o['items'][i]==men['name']:
#                         total=total+men['price']
#     return total
# print('you should pay:'+str(billcompute(x))+'$')
connect_to_salary=db['salary']
all_salary=connect_to_salary.find()
for x in all_salary:
    print(x)
# def insert_lecture():
#     a,b,c=input('plz enter your information:').split(' ')
#     connect_to_salary.insert({
#         'name':a,
#         'session':int(b),
#         'salary/session':int(c)
#     })
# insert_lecture()
# def payroll():
#     x= input('name plz:')
#     all_salary = connect_to_salary.find()
#     for a in all_salary:
#         if a['name']==x:
#             return int(a['session'])*int(a['salary/session'])
# print(payroll())
a=connect_to_salary.update_one(
    {'name':'lalala'},
    {'$set':{
        'session':1000},
    '$currentDate':{'lastModified':True}
    }
)
