from firebase import firebase
from time import sleep

fb = firebase.FirebaseApplication('https://hiepxanh.firebaseio.com/user/',None)
# mychat = fb.post('/user',{'name':'Khanh','text':'this is a chat program'})
response = fb.get('/user',None)
chatList = response.items()
for key,value in chatList:
    print (value['name'],':',value['text'])

while True:
    mychat = input('Khanh: ')
    if mychat == None:
        pass
    else:
        postChat = fb.post('/user',{'name':'Khanh','text':str(mychat)})

    if key, value not in chatList:
        print(value['name'], ':', value['text'])
        chatList = chatList.append(key,value)