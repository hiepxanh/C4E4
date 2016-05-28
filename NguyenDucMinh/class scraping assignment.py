from urllib import request
import bs4

link="http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2015/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
r=request.urlopen(link)
html_source=r.read()

soup=bs4.BeautifulSoup(html_source,'html.parser')
table=soup.find_all('table',{'id':'tableContent'})
td = soup.find_all("td", {"class": "b_r_c"})
td2=soup.find_all("td",{"class":"h_t"})
for i in td:
      print(i.string)
    


    
    
