#coding:utf-8
import unittest
from public import Excel
import ddt
import requests
import json
import time
import sys
sys.path.append("..")
from DATA import DATA

def user(method,data):
    result = requests.post(method,data= data)
    return result

u'''
token有效性验证:  validateToken   String phone, String token
用户信息 : userInfo    String phone, String token
登录 : login   String phone,String securityCode,String terminal,Integer loginDevice
修改头像:  modifyHeadImage   String token, String phone
我的家属 : myFamily
留言列表 : wordsList   String token, String phone, Integer pageNo
用户留言  :  leaveWords   String token, String phone,String content
data = {"phone":"17761196077","token":"1f7e0db62349483d9f0b43dbd6318985_app"}
'''

data = {"phone":"17761196077","token":"1f7e0db62349483d9f0b43dbd6318985_app"}
method = DATA.myFamily()
result = user(method,data)
print result._content