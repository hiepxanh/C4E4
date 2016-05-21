import pymongo

db_uri="mongodb://c4e:codethechange@ds021922.mlab.com:21922/cafeteria"
db=pymongo.MongoClient(db_uri).get_default_database()

salary = db['salary']
s = salary.find()

# input = input("Enter: ")
# def insert_lecturer():
#     l = input.split()
#     salary.insert_one(
#         {
#             'name' : l[0],
#             'salary/session': l[1],
#             'session': l[2]
#         }
#     )
#     for x in s:
#         print (x)
# insert_lecturer()
# n  = input("name :")
# def Payroll(n):
#     for x in s:
#         if n == x['name']:
#             a = int(x['salary/session']) * int(x['session'])
#             print ("Tong luong" ,x['name'],":", a )
# Payroll(n)
result = salary.update_one(
    {"name": "tu"},
    {
        "$set": {
            "name" :"hoang",
            "salary/session": 200,
            "session": 100
        },
    }
)
salary.delete_one({'name':'lalala'})
for x in s:
    print (x)


while True:
    f = input("Choose: Create, Read, Update, Delete: ")
    if f == "Create":
        def create(x, y, z):
            salary.insert_one({"name": x,
                               "session": y,
                               "salary/session": z})
            print(salary.find_one({"name": x}))

        i = input("Create : ")
        l=i.split()
        create(l[0],l[1],l[2])

    elif f == "Read":
        def read(r1):
            r1 = salary.find_one({"name": r1})
            print ("The person {0}'s number of session is ".format(r1["name"]) + r1['session'])
            print ("The person {0}'s salary/session is ".format(r1["name"]) + r1['salary/session'])
        read = input("Enter the name : ")


        if salary.find_one({"name": read})!=None:
            read(read)
        else:
            print("Wrong name")

    elif f == "Update":
        def update(x, y, z):
            salary.update_one({
                "name": x
            }, {
                "$set": {
                    "session": y,
                    "salary/session": z}
            })
            u = salary.find_one({"name": z})
            print(u)
        update = input("Update : ")
        update = update.split()
        update(update[0],update[1],update[2])

    elif f == "Delete":
        def delete(d):
            salary.delete_one({"name": d})
            if salary.find_one({'name': d}) == None:
                print(d + " removed")

            delete = input("Delete: ")
            delete(delete)

    else:
        print("Wrong")
