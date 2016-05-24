from firebase import firebase
# fb = firebase.FirebaseApplication("https://techkids-c4e.firebaseio.com", None)
# result = fb.post('/',{
#     'name':"Hau",
#     "title":'dont kill me',
#     'content':'x',
#     'image':'http://vi.rayarkgames.wikia.com/wiki/T%E1%BA%ADp_tin:Winter_(Deemo_ver.).png'
# })
from firebase import firebase
from time import*
fb=firebase.FirebaseApplication('https://hiepxanh.firebaseio.com/user/',None)
respone=fb.get('/user',None)
print(type(respone))
# respone=fb.post('/user',{
#     'name':'hahaha',
#     'text':'yeu cau di an'
# })
def getallchat():
    respone=fb.get('/user',None)
    for x,y in respone.items():
        print(str(y['name'])+':'+str(y['text']))
def get_current_chat(a):
    respone=fb.get('/user',None)
    for b in respone.keys():
        if b not in a:
            print(str(respone[b]['name'])+':'+str(respone[b]['text']))
getallchat()
while True:
    a = fb.get('/user', None)
    sleep(5)
    print(len(a))
    get_current_chat(a)
print(respone)