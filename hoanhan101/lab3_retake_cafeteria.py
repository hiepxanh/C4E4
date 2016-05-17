import pymongo

uri = "mongodb://c4e:codethechange@ds021922.mlab.com:21922/cafeteria"
client = pymongo.MongoClient(uri)

db = client.get_default_database()

salary_collection = db["salary"]

all_salary = salary_collection.find()
for salary in all_salary:
    print(salary["name"],"taught:",salary["session"],"salary:",salary["salary/session"])

def insert_lecturer():
    name,session,salary = input("Please enter your information:").split()
    salary_collection.insert_one(
        {"name":name,
         "session":session,
         "salary/session":salary}
    )
    print(name,"taught:",session,"salary:",salary)

def Payroll():
    total = 0
    name = input("Which one you want to know the total salary?")
    all_salary = salary_collection.find()
    for salary in all_salary:
        if salary["name"] == name:
            total = int(salary["session"]) * int(salary["salary/session"])
    print(name, "total salary is:",total)

def update_info():
    name,session,salary = input("Enter information you need to update:").split()
    salary_collection.update_one(
        {"name":name},
        {"$set":
             {"session":session,
              "salary/session": salary}}
    )
    print("updated:",name,"taught:",session,"salary:",salary)

def delete_name():
    name = input("Which one do you ned to delete?")
    salary_collection.delete_one({"name":name})
    print(name, "deleted!")

print("Hello, this is a salary program.")
while True:
    select_function = input("Please select your function (Create,Read,Update,Delete):")
    if select_function == "Create":
        insert_lecturer()
    if select_function == "Read":
        Payroll()
    if select_function == "Update":
        update_info()
    if select_function == "Delete":
        delete_name()

