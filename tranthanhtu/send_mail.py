import smtplib
import pyexcel as pe
import pyexcel.ext.xlsx

def send_email(message, rev):
    username = "practice.c4e"
    password = "codethechange"
    email_helper = smtplib.SMTP('smtp.gmail.com:587')
    email_helper.starttls()
    email_helper.login(username,password)
    email_helper.sendmail("practice.c4e@gmail.com", rev,message)
    email_helper.quit()
records = pe.get_records(file_name="info.xlsx")
for record in records:
    n = record['Name']
send_email("Subject :"+ n +"oi\nTran Thanh Tu",record['Email'])


# class calculateDistance(city):
#     hanoi = {"name" : "Ha Noi", "longt: 50, "lat" : 75}
#     daiduong = {"name": "Hai Duong", "longt: 25, "lat" : 10}
#     def __init__(self, name, longt, lat ):
#         self.name = name
#         self.longt = longt
#         self.lat = lat
#     def distance(self):
# class City:
#     def __init__(self, name, longt, lat):
#         self.name = name
#         self.longt = longt
#         self.lat = lat
#     def calculateDistance(self, anotherCity):
#         longt1 = self.longt
#         longt2 = anotherCity.longt
#         lat1 = self.lat
#         lat2 = anotherCity.lat
#
#         return (((longt1 - longt2)**2 + (lat1 - lat2)**2)**0.5)
# hanoi = City("hanoi",75,50)
# haiduong = City("haiduong",25,10)
# distance = hanoi.calculateDistance(haiduong)
# print(distance)





