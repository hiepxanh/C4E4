from urllib import request
import bs4
import pyexcel
import pyexcel.ext.xlsx

link = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2015/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
r = request.urlopen(link)
html_source = r.read()
soup = bs4.BeautifulSoup(html_source, "html.parser")
table = soup.find("table", {"id":"tableContent"})

list_rows=[]
rows1 = table.find_all("tr", {"class":"r_item "})
for row1 in rows1:
    list_rows.append(row1)
rows2 = table.find_all("tr", {"class":"r_item_a "})
for row2 in rows2:
    list_rows.append(row2)

l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
l6 = []
for row in list_rows:
    list_strings = []
    columns = row.find_all("td", {"class":"b_r_c"})
    for column in columns:
        list_strings.append(column.string)
    l1.append(list_strings[0])
    l2.append(list_strings[1])
    l3.append(list_strings[2])
    l4.append(list_strings[3])
    l5.append(list_strings[4])
    l6.append(list_strings[5])

TableExcel = {" ": l1, "Column 2": l2, "Column 3": l3, "Column 4":l4, "Column 5":l5, "Column 6":l6}
sheet = pyexcel.get_sheet(adict=TableExcel)
sheet.save_as("TableTest.xlsx")









#print ra toan bo Column 1

#
# for row in rows:
#     list = []
#     columns = row.find_all("td")
#     for column in columns:
#         list.append(column)
#         print (list[0].string)
#


# li_s = ul.find_all("li")
#     print(li.h2.a.string)
