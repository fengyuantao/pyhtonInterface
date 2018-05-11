#coding:utf-8
from public import Excel

import requests
import json
import time
import sys
from public import get_log
sys.path.append("..")
from DATA import DATA
## 获取验证码码
#login
logger = get_log
phone = "18602876515"

sendCode = requests.post(DATA.sendSecurityCode(),data={'phone':phone})
logger.insertLog(sendCode.url,phone,sendCode.text)

securityCode = raw_input("securityCode:")

data1 = {'phone':phone,'code':securityCode}
validateCode = requests.post(DATA.validateCode(),data=data1)
validateStr =  validateCode.json()["data"]

logger.insertLog(DATA.validateCode(),data1,validateCode.text)

url = DATA.register()
data = {'phone':phone,'activeCode':'708288','validateStr':validateStr,'terminal':'app','loginDevice':2}

result = requests.post(url=url,data=data)
logger.insertLog(url,data,result.text)

'''

login = requests.post(DATA.login(),data={'phone':phone,'securityCode':securityCode,'terminal':'app','loginDevice':2})
print login._content
'''



