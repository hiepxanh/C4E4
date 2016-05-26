
from urllib import request
import bs4
import pymongo

link = "http://vietnamnet.vn/vn/kinh-doanh/tai-chinh/"
uri = "mongodb://c4e:codethechange@ds011893.mlab.com:11893/c4e_rss"
client = pymongo.MongoClient(uri)
db = client.get_default_database()
db_posts = db['posts']

r = request.urlopen(link)  ## connect to dantri.com
html_source = r.read()
soup = bs4.BeautifulSoup(html_source, "html.parser")
posts = soup.find_all('li', {"class" : "item clearfix dotter"})
for post in posts:
    link = 'http://vietnamnet.vn' + post.a['href']

    title = post.a['title'] + ' Mai Huong'

    db_posts.insert_one(
        {'title': title,
         'link': link,
         }
    )

