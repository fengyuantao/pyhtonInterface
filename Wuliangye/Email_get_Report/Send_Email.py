#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import time
class Email(object):
    def __init__(self,base_dir,mail_to,subject,data):
        self.base_dir = base_dir
        self.__sender = "fengyuantao@hexinpass.com"
        self.__password = "111111feng"
        self.mailTo = mail_to
        self.subject = subject
        self.data = data
        self.Server = "mail.hexinpass.com"
        self.status = False
    def Send(self):
        fp = open(self.base_dir,'rb')
        mail_body = fp.read()
        fp.close()
        #创建一个带附件的实例
        try:
            msg = MIMEMultipart('alternative')
            part = MIMEText(mail_body,'html')
            msg.attach(part)
            msg['date'] = Header(self.data,'utf-8')
        #定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
            msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
            msg['subject'] = Header(self.subject,'GBK')

            smtp = smtplib.SMTP()
            smtp.connect(self.Server)
            smtp.login(self.__sender,self.__password)
            smtp.sendmail(self.__sender,self.mailTo,msg.as_string())
            smtp.quit()
            self.status = True
        except Exception:
            self.status = False
        return self.status
