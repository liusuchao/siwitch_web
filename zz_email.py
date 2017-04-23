#coding:utf-8

from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText

mail_info = {
    "from": "314462545@qq.com",
    "to": "314462545@qq.com",
    "hostname": "smtp.qq.com",
    "username": "314462545@qq.com",
    "password": "asjxdyqetcenbgdj",
    "mail_subject": "深圳众智家电子有限公司",
    "mail_text": "verify:",
    "mail_encoding": "utf-8"
}
def send_verify(to_email,code):
    mail_info["to"] = to_email   
    mail_info['mail_text'] = "verify:" + code 
    smtp = SMTP_SSL(mail_info["hostname"])
    #smtp.set_debuglevel(1)
    smtp.ehlo(mail_info["hostname"])
    smtp.login(mail_info["username"], mail_info["password"])
    msg = MIMEText(mail_info["mail_text"], "plain", mail_info["mail_encoding"])
    msg["Subject"] = Header(mail_info["mail_subject"], mail_info["mail_encoding"])
    msg["from"] = mail_info["from"]
    msg["to"] = mail_info["to"]
    smtp.sendmail(mail_info["from"], mail_info["to"], msg.as_string())
    smtp.quit()	

