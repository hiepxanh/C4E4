from urllib import request
import bs4

link = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2015/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

r = request.urlopen(link)
html_source = r.read()

soup = bs4.BeautifulSoup(html_source, 'html.parser')
table = soup.find('table', {"id" : "tableContent"})

trs = table.find_all('tr')
for tr in trs:
    tds = tr.find_all('td', {"class" : "b_r_c"})
    for td in tds:
        print(td.text)

