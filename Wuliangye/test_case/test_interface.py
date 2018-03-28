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
sendCode = requests.post(DATA.sendSecurityCode(),data={'phone':'15680785518'})
securityCode = raw_input("securityCode:")
'''
validateCode = requests.post(DATA.validateCode(),data={'phone':'15680785518','code':securityCode})
print validateCode._content
'''

login = requests.post(DATA.login(),data={'phone':'15680785518','securityCode':securityCode,'terminal':'app','loginDevice':2})
print login._content



url = DATA.register()
data = {'phone':'15680785518','activeCode':'152365','validateStr':securityCode,'terminal':'app','loginDevice':2}

result = requests.post(url=url,data=data)
print result._content