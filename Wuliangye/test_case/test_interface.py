#coding:utf-8
from public import Excel

import requests
import json
import time
import sys
sys.path.append("..")
from DATA import DATA
## 获取验证码码
#login
sendCode = requests.post(DATA.sendSecurityCode(),data={'phone':'17761196077'})
securityCode = raw_input("securityCode:")


validateCode = requests.post(DATA.validateCode(),data={'phone':'17761196077','code':securityCode})
validateStr =  validateCode.json()["data"]
print validateCode._content
url = DATA.register()
data = {'phone':'17761196077','activeCode':'914299','validateStr':validateStr,'terminal':'app','loginDevice':2}

result = requests.post(url=url,data=data)
print result._content

'''
login = requests.post(DATA.login(),data={'phone':'17761196077','securityCode':securityCode,'terminal':'app','loginDevice':2})
print login._content
'''



