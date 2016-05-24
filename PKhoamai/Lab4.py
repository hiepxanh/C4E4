# class my_shapes:
#     def __init__(self,sides):
#         self.sides=sides
# my_square = my_shapes(4)
# print(my_square.sides)
#
# class Pet():
#     is_alive = True
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def eat(self,food):
#         if food =="catnip":
#             print("I'am getting high")
#         elif food =="fish":
#             print("Wonderful")
#         else:
#             print("That's good")
#
#
# cat=Pet("kitty",2,)
# print(cat.name,"\n",cat.age,cat.is_alive)
# cat.name="mimi"
# print(cat.name,"\n",cat.age)
# cat.eat("fish")

# from firebase import firebase
# fb=firebase.FirebaseApplication("https://techkids-c4e.firebaseio.com",None)
# result=fb.post("/",{"name":"PK Beu","title":"alo picaso","content":"7D","image":"https://www.google.com/search?q=PK&oq=PK&aqs=chrome..69i57j69i60l5.2591j0j9&sourceid=chrome&ie=UTF-8"})
# print(result)

from firebase import firebase
from time import sleep
from pprint import pprint
fb=firebase.FirebaseApplication("https://hiepxanh.firebaseio.com/user/",None)
response=fb.get('/user',None)
sleep(10)
pprint(response)

print(response)
for key, value in response.items():
    print(value)
    print(value["name"],": ",value['text'])




# from twilio.rest import TwilioRestClient
# account_sid = "ACc0aa18c224fa2d295957d2dbd5c0ceaa"
# auth_token  = "4a0f9c6bf82500bb816b04738f00e7b5"
# client=TwilioRestClient(account_sid, auth_token)
#
# message=client.messages.create(to="+84945671992",from_="+12102390636",body ="Oil for Hiepdamdang")
