import smtplib
import pyexcel as pe
import pyexcel.ext.xlsx

def send_email(mes,rev):
    username = "practice.c4e"
    password = "codethechange"

    email_helper = smtplib.SMTP("smtp.gmail.com:587")
    email_helper.starttls()
    email_helper.login(username,password)
    email_helper.sendmail("practice.c4e@gmail.com",rev,mes)
    email_helper.quit()

records = pe.get_records(file_name="info.xlsx")
for record in records:
    send_email("Subject: Test\nGotit?",record["Email"])

