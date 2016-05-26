from urllib import request
import bs4
import pymongo

link = 'http://m.vietnamnet.vn/'
uri = 'mongodb://c4e:codethechange@ds011893.mlab.com:11893/c4e_rss'

client = pymongo.MongoClient(uri)
db = client.get_default_database()
db_posts = db['posts']

r = request.urlopen(link)
html_source = r.read()

soup = bs4.BeautifulSoup(html_source,'html.parser')
hot_posts = soup.find_all('div',{"class":"post-right"})
i = 1
for post in hot_posts:
    title = post.h6.a.string + ' by Khanh'
    print(title)
    link = 'http://m.vietnamnet.vn' + post.h6.a['href']
    print(link)
    #db_posts.insert_one({'title':title,'link':link})
    print('--------------------------')
    i += 1
    if i > 5: break
