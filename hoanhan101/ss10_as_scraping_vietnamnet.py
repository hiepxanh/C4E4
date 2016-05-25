from urllib import request
import bs4
import pymongo

db_uri = "mongodb://c4e:codethechange@ds011893.mlab.com:11893/c4e_rss"

db = pymongo.MongoClient(db_uri).get_default_database()
db_posts = db["posts"]

link = "http://vietnamnet.vn"

r = request.urlopen(link)
html_source = r.read()
print(html_source)

soup = bs4.BeautifulSoup(html_source, "html.parser")

posts = soup.find("ul", {"class":"HotList"})
for post in posts:
    link = "http://vietnamnet.vn" + post.h2.a["href"]
    title = "hoanhan101: " + post.h2.a.string
    print(title)
    print(link)
    db_posts.insert_one(
        {
            "title:":title,
            "link": link
        }
    )

