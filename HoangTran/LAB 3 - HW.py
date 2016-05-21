import pymongo

uri = "mongodb://c4e:codethechange@ds021922.mlab.com:21922/cafeteria"
client = pymongo.MongoClient(uri)
db = client.get_default_database()

salary = db['salary']

# testing=salary.find_one({"name":"Testing"})
# print(testing['session'])

def payroll(name):
    p = salary.find_one({"name":name})
    p1 = int(p['session'])*int(p['salary/session'])
    print ("Total salary of {0} is {1}".format(p["name"], p1))

# PAYROLL
# name = input("Input your name: ")
# payroll(name)

print("Hello, this is the Salary Program")
while True:
    ifinal = input("Please select your function by typing: Create, Read, Update, Delete: ")
    if ifinal == "Create":
        def create(c1, c2, c3):
            salary.insert_one({"name": c1,
                               "session": c2,
                               "salary/session": c3})
            print(salary.find_one({"name": c1}))

        i = input("Create your own dictionary by inputing Name/Session/Salary: ")
        l=i.split()
        create(l[0],l[1],l[2])

    elif ifinal == "Read":
        def read(r1):
            r1 = salary.find_one({"name": r1})
            print ("The person {0}'s number of session is ".format(r1["name"]) + r1['session'])
            print ("The person {0}'s salary/session is ".format(r1["name"]) + r1['salary/session'])
        iread = input("Enter the name of the person you wish to show up: ")


        if salary.find_one({"name": iread})!=None:
            read(iread)
            payroll(iread)
        else:
            print("Wrong name")

    elif ifinal == "Update":
        def update(u1, u2, u3):
            salary.update_one({
                "name": u1
            }, {
                "$set": {
                    "session": u2,
                    "salary/session": u3}
            })
            u = salary.find_one({"name": u1})
            print(u)
            print("Updated")
        iupdate = input("Update your info by inputing Name/Session/Salary: ")
        lupdate = iupdate.split()
        update(lupdate[0],lupdate[1],lupdate[2])

    elif ifinal == "Delete":
        def delete(d1):
            salary.delete_one({"name": d1})
            if salary.find_one({'name': d1}) == None:
                print(d1 + " has been deleted")

            idelete = input("Enter the name you wish to delete: ")
            delete(idelete)

    else:
        print("Wrong function name, please retry!")







