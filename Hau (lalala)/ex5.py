# filmdict={
#     'name:':'the Crank',
#     'year:':1997
# }
# n=''
# list_of_film=[filmdict]
# while n!='stop' and n!='no':
#     x=input('name of film:')
#     y=input('release date:')
#     sampledict={
#         'name:':x,
#         'year:':y
#     }
#     list_of_film.append(sampledict)
#     n=input('wanna continue? ')
# for x in list_of_film:
#     for y,z in x.items():
#         print(y,z)
# def film_finder(list_of_film,keyword,typeofkeyword):
#     for x in list_of_film:
#         for y,z in x.items():
#             if y==typeofkeyword:
#                 if z==keyword:
#                     print(y,z)
# a=input('type u want to find:')
# b=input('name of film:')
# film_finder(list_of_film,b,a)
# def killfilm(list_of_film):
# inventory = {
#     'gold': 500,
#     'pouch': ['flint', 'twine', 'gemstone'],
#     'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
#  }
# inventory2={
#     'pocket':['seashell','strange berry','lint']
# }
# for x,y in inventory.items():
#     if x=='backpack':
#         y.sort()
#         y.remove('dagger')
#     elif x=='gold':
#         inventory['gold']=y+50
#
# inventory.update(inventory2)
# print(inventory)
prices={
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stock = {
    "banana": 6,
    "apple": 4,
    "orange": 32,
    "pear": 15
}
def display(prices,stock):
    for x,y in prices.items():
        print('\n'+x+':')
        print('price:'+str(y))
        for z,w in stock.items():
            if z==x:
                print('stock:'+str(w))
def total_profit(prices,stock):
    total=0
    for x,y in prices.items():
        for z,w in stock.items():
            if x==z:
              total=total+y*w
    return total
def bill_compute(prices,stock,dict_of_buying_item):
    spend=0
    a=False
    for x,y in dict_of_buying_item.items():
        for z,w in stock.items():
            if x==z:
                a=True
                if (int(y)-int(w))>0:
                    return 'not enough in stock'
                    break
                else:
                    stock[z]=int(w)-int(y)
        if a==True:
            for d, c in prices.items():
                if x == d:
                    spend = c * y
        else:
            return 'no fruit chosen'
    return spend

display(prices,stock)
print('if we sold all in stock we got ',total_profit(prices,stock))
a='False'
dict_of_buying_item={

}
while a!='no':
    a=input('which ones u want to buy? ')
    b=int(input('how many? '))
    tempdict={
        a:b
    }
    dict_of_buying_item.update(tempdict)
    a=input('wanna continue? ')
if bill_compute(prices,stock,dict_of_buying_item)=='no fruit chosen':
    print('no fruit chosen')
elif bill_compute(prices,stock,dict_of_buying_item)=='not enough in stock':
    print('not enough in stock')
else:
    print('u spend '+str(bill_compute(prices,stock,dict_of_buying_item))+' dollar')