import pymongo
uri = "mongodb://c4e:codethechange@ds021922.mlab.com:21922/cafeteria"
client = pymongo.MongoClient(uri)
db = client.get_default_database()
salary_collection = db['salary']
# salary = salary_collection.find()
# for i in salary:
#     print(i)
# for i in salary:
#     print(i['name'], "taught :", i['session'], 'salary:', i['salary/session'])

# n = input("please enter your information")
# x, y, z = input(n).split()
# print(x,y,x)
# print(x, 'taught: ', y, "salary: ", z)

# salary_collection.insert_one(
#     {'name': 'Huong',
#      'session' : 10,
#      'salary/session' : 110}
# )

# salary = salary_collection.find()
# for i in salary:
#     print(i)
## print out all item again
# x, y, z= input("Please enter your information: ").split()
#
# def data_insert(x, y, z):
#     salary_collection.insert_one(
#         {'name': x,
#          'session' : y,
#          'salary/session' : z}
#     )
# data_insert(x, y, z)
# salary = salary_collection.find()
# for i in salary:
#     print(i)

# n = input("Enter lecturer's name: ")
# def payroll(n):
#     lecturer_name = salary_collection.find({'name': n})
#     for i in lecturer_name:
#         if n == i['name']:
#             total = int(i['session'])* int(i['salary/session'])
#             return total
#         else:
#             print('Khong co du lieu')
#
# print(payroll(n))

# x,y, z = input("Enter information: ").split()
# def data_update(x, y, z):
#     salary_collection.update_one(
#         {'name': x},
#         {
#             "$set":
#                 {'session' : y,
#                 'salary/session' : z}
#         }
#     )
# data_update(x, y, z)

# salary = salary_collection.find()
# for i in salary:
#     print(i)

# n = input("Which one do you need to delete: ")
# def delete_lecturer(n):
#     salary_collection.delete_one({'name': n})
#     return
# delete_lecturer(n)
# lecturer_find = salary_collection.find_one({'name': n})
# a = print(lecturer_find)
# if a == None:
#     print(n, "is deleted")
# else:
#     print("Oops, bugs detected")

## wave 7
def payroll(n):
    lecturer_name = salary_collection.find({'name': n})
    for i in lecturer_name:
        if n == i['name']:
            total = int(i['session'])* int(i['salary/session'])
            return total
        else:
            print('Khong co du lieu')

#
def data_insert(x, y, z):
    salary_collection.insert_one(
        {'name': x,
         'session' : y,
         'salary/session' : z}
    )

def data_update(x, y, z):
    salary_collection.update_one(
        {'name': x},
        {
            "$set":
                {'session' : y,
                'salary/session' : z}
        }
    )

def delete_lecturer(n):
    salary_collection.delete_one({'name': n})


print("Hello, this is salary program")
while True:
    a = input("Please, select your function (Create, read, update, delete): ")
    if a == "read":
        n = input("Enter your lecturer's name: ")
        print("Your salary is: ", payroll(n))
    elif a == 'create':
        x, y, z= input("Please enter information you want to insert: ").split()
        data_insert(x, y, x)
        salary = salary_collection.find_one({'name' : x})
        print(salary)

    elif a == 'update':
        x,y, z = input("Enter information you want to update: ").split()
        data_update(x, y, z)
        salary = salary_collection.find_one({'name': x})
        print(salary)
    elif a == 'delete':
        n = input("Which one do you need to delete: ")
        delete_lecturer(n)
        print(n, "is deleted")




