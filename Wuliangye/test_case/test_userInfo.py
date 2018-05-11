#coding:utf-8
import unittest
from public import Excel
import ddt
import requests
import json
import time
import logging
import sys
sys.path.append("..")
from DATA import DATA
from public.get_log import insertLog

def user(method,data):
    result = requests.post(method,data= data)
    return result

u'''
token有效性验证:  validateToken   String phone, String token
用户信息 : userInfo    String phone, String token
登录 : login   String phone,String securityCode,String terminal,Integer loginDevice ,String deviceNo
修改头像:  modifyHeadImage   String token, String phone
我的家属 : myFamily
留言列表 : wordsList   String token, String phone, Integer pageNo
用户留言  :  leaveWords   String token, String phone,String content
data = {"phone":"17761196077","token":"1f7e0db62349483d9f0b43dbd6318985_app"}
{"phone":"15680785518","token":"2a7570e2fec348e1b91df961ccf8ee0e_app"}

230604199504114450
'''

data2 = {"phone":"15680785518","token":"2a7570e2fec348e1b91df961ccf8ee0e_app"}
data1 = {"phone":"17761196077","token":"1f7e0db62349483d9f0b43dbd6318985_app"}
wordsList = {"phone":"17761196077","token":"1f7e0db62349483d9f0b43dbd6318985_app",'securityCode':'941196'}
method = DATA.leaveWords()
#941196
wallet = DATA.Wallet()

result = user(wallet.forgetPayPassword,wordsList)
print 'url*****************************************************%s'%result.url

insertLog(wallet.forgetPayPassword,wordsList,result.text)
