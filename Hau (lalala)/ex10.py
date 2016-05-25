import pymongo
db_uri='mongodb://c4e:codethechange@ds021922.mlab.com:21922/cafeteria'
db=pymongo.MongoClient(db_uri).get_default_database()#mongo data
from urllib import request
import bs4
db_post=db['posts']
link='http://vietnamnet.vn/vn/thoi-su/'#link
r=request.urlopen(link)
html_source=r.read()
# print(html_source)
soup=bs4.BeautifulSoup(html_source,'html.parser')#just remember

post=soup.find_all('li',{'class':"item clearfix dotter"})#search element li and a value
for po in post:

    print('-----------------------------')
    a_tags=po.find('a')
    for atag in a_tags:
        print(atag)
    print(po.a)

    print(po.a['href'])
    print(po.a['title'])
    print(po.a.img['src'])
    print('----------------------')
    links='https://dantri.com.vn'+po.a['href']
    title=po.a['title']+'cua ai :))'
    img=po.a.img['src']

    db_post.insert_one({
        'title':title,
        'link':links,
        'img':img
    })

    print(po.a['href']['img'])
print(type(post))
