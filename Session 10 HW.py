from urllib import request
import bs4
import pymongo
link = "http://vietnamnet.vn/"
uri="mongodb://c4e:codethechange@ds011893.mlab.com:11893/c4e_rss"
client = pymongo.MongoClient(uri)
db=client.get_default_database()
db_posts=db["post"]

r=request.urlopen(link)
html_source = r.read()

soup = bs4.BeautifulSoup(html_source, ['html.parser'])
posts = soup.find_all("div",{"class":"Main-Body w-1000"})
for post in posts:
    print(post)
    a_tags=post.find_all("a")
    for a_tag in a_tags:
        print(a_tag)
    print(post.a['href'])
    print(post.a["title"])
    print(post.a.img['src'])
    link="http://vietnamnet.vn/" + post.a["href"]
    title=post.a["title"]+"PK"
    img=post.a.img['src']
    db_posts.insert_one(
        {
            "title":title,
            "link":link,
            "img":img
        }
    )
