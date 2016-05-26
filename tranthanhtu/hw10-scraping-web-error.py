from urllib import request
import bs4
import pymongo
link = "http://vietnamnet.vn/"
uri = "mongodb://c4e:codethechange@ds011893.mlab.com:11893/c4e_rss"
client = pymongo.MongoClient(uri)
db = client.get_default_database()
db_posts = db["posts"]
r = request.urlopen(link)
html_source = r.read()

soup = bs4.BeautifulSoup(html_source,"html.parser")
posts = soup.find_all("div", {"class":"HomeTopCenter left"})
for post in posts:
    link = post.div.a["href"]
    img  = post.div.img["src"]
    db_posts.insert_one(
        {
            "link":link,
            "img":img
        }
    )
posts2 = soup.find("ul", {"class":"HotList"})
for post2 in posts2:
    link = ("http://vietnamnet.vn" + post2.li.h2.a["href"] + "by Tran Thanh Tu")
    title = post2.li.h2.a.string
    db_posts.insert_one(
        {
            "link":link,
            "title":title
        }
    )