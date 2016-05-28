from urllib import request
import bs4
import pymongo
link = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2015/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
uri = "mongodb://c4e:codethechange@ds011893.mlab.com:11893/c4e_rss"
client = pymongo.MongoClient(uri)
db = client.get_default_database()
db_posts = db["posts"]
r = request.urlopen(link)
html_source = r.read()
soup = bs4.BeautifulSoup(html_source,"html.parser")
trs = soup.find_all("tr")
for tr in trs:
    list_td = tr.find_all('td',{'class':'b_r_c'})
    for text in list_td:
        print(text.get_text())






