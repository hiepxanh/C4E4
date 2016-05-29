from urllib import request
import bs4
import pyexcel
import pyexcel.ext.xlsx

link = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2015/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

r = request.urlopen(link)
html_source = r.read()
soup = bs4.BeautifulSoup(html_source, "html.parser")

list = []
l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
l6 = []

td = soup.find_all("td", {"class": "b_r_c"})
for i in td:
    list.append(i.string)

for i in range(0,len(list),6):
    l1.append(list[i])
for i in range(1,len(list),6):
    l2.append(list[i])
for i in range(2,len(list),6):
    l3.append(list[i])
for i in range(3,len(list),6):
    l4.append(list[i])
for i in range(4,len(list),6):
    l5.append(list[i])
for i in range(5,len(list),6):
    l6.append(list[i])

cafebiz_report = {"":           l2,
                  "Quý 4-2014": l3,
                  "Quý 1-2015": l4,
                  "Quý 2-2015": l5,
                  "Quý 3-2015": l6,
                  "Tăng trưởng":l1
                  }
sheet = pyexcel.get_sheet(adict=cafebiz_report)
sheet.save_as("cafebiz_report.xlsx")
