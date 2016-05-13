import pymongo
db_uri = "mongodb://c4e:codethechange@ds021922.mlab.com:21922/cafeteria"
db=pymongo.MongoClient(db_uri).get_default_database()
menu= db["menu"]


m = menu.find()
for x in m:
    print(x)


blcf = menu.find({'name' : 'black coffee'})
for i in blcf:
    print(i['name'])
chip = menu.find({'name' : 'chips'})
for j in chip:
    print (j['name'])
redtea = menu.find({'name' : 'red tea'})
for q in redtea:
    print (q['name'])

print ("Hiep : ", [i['name'],j['name']])
print ("Huy : ", [q['name']])

menu.insert_one({
    'name' : 'capuchino'
})
cp = menu.find({'name' : 'capuchino'})
for p in cp:
    print("Tu : ", [p['name']])

print ("Hiep oder: ",[i['name'],j['name']] )
pay = i['price'] + j['price']
print (pay)
print ("Hiep paid : ",pay)
