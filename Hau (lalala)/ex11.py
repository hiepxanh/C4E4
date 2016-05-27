import pymongo
db_uri='mongodb://c4e:codethechange@ds021922.mlab.com:21922/cafeteria'
db=pymongo.MongoClient(db_uri).get_default_database()#mongo data
from urllib import request
import bs4
db_post=db['posts']
link='http://s.cafef.vn/bao-cao-tai-chinh/PPC/IncSta/2018/4/0/0/1/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-nhiet-dien-pha-lai.chn'#link
r=request.urlopen(link)
html_source=r.read()
# print(html_source)
soup=bs4.BeautifulSoup(html_source,'html.parser')#just remember-----we are at body
ul=soup.find('form',{'id':'form1'})#we are at ul------>>go to li
a=ul.find('div',{'id':'divTop'})#come for a now
b=a.div.div.find('div',{'class':'cf_BoxContent'})
c=b.find('div',{'class':'cf_ResearchDataHistoryInfo'})
d=c.find('div',{'align':'left'})
e=d.find('div',{'style':'overflow:hidden;width:100%;border-bottom:solid 1px #cecece;'})
f=e.find_all('tr')
# for x in f:
#     print(x.td.string)
g=[]

for x in f:
    b=x.find_all('td',{'class':'b_r_c'})
    a=0
    for m in b:
        print(m.get_text())
        g.append(m.get_text())

# print(g)
# for h in g:
#     print(h.string)
fo