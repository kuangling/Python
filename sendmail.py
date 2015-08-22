#!/usr/local/bin/python
#-*- coding:utf-8 -*-
import sys
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

if len(sys.argv)!=4:
    print "参数错误，请使用:%s table_con html_tr_content mail_header"%sys.argv[0]
    sys.exit(1)
table_header=sys.argv[1]
content1=sys.argv[2]
mail_header=sys.argv[3]
if content1.strip()!="" and table_header.strip()!="":
    content='''
    <html>\n
    <head><title>'''+table_header+'''</title>\n
    <body>\n
    <table border=1 cellpadding="0" cellspacing="0">\n
    <tr><th colspan='4' style=\"background:black;color:white;\">'''+table_header+'''</th></tr>\n
    '''+content1+'''
    </table>\n
    </body>\n
    </html>
    '''
    mail_list=["admin@test.com"]
    msg=MIMEMultipart()
    msg['Accept-Language']='zh-CN'
    msg['Accept-Charset']= 'ISO-8859-1,utf-8'
    msg['From']="monitor@test.com"
    msg['to']=";".join(mail_list)
    msg['Subject']=mail_header.decode("utf-8")+u'['+time.strftime('%Y-%m-%d %H:%M',time.localtime())+']'
    txt=MIMEText(""+str(content)+"",'html','utf-8')
    txt.set_charset('utf-8')
    msg.attach(txt)
    smtp=smtplib.SMTP("mail.test.com")
    smtp.sendmail(msg["From"],mail_list,msg.as_string())
    smtp.close()
