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
from public.get_log import insertLog

def transfer(method,data): ###  转账
    url = DATA.payOrder()

    result = requests.post(url.__dict__[method],data)
    return result

def wallit(method,data):  ### 支付相关
    url = DATA.Wallet()
    result = requests.post(url.__dict__[method],data)
    return result
'''
setPayPassword_data = {"phone":"17761196077","token":"1f7e0db62349483d9f0b43dbd6318985_app","payPassword":"12346"}
method = "setPayPassword"
result = wallit(method,setPayPassword_data)
'''

'''
data = {"phone":"17761196077","token":"1f7e0db62349483d9f0b43dbd6318985_app","familyPhone":"15680785518","transferAmount":100,"payPwd":"123456"}
method = "transferFamily"

'''
u"""
验证是否有支付密码：hasPayPassword   String phone, String token
设置支付密码：  setPayPassword   String phone, String token  String payPassword
忘记支付密码： forgetPayPassword  String phone,String token,String securityCode
重置支付密码： resetPayPassword   String token,String phone,String validateStr,String payPassword
修改支付密码： modifyPayPassword  String phone,String token,String oldPayPassword,String newPayPassword
验证支付密码： payValidate        String token,String payPassword,String phone
设置免密支付： setNoPass          String token,String phone,String payPassword,Integer noPass
判断免密支付： hasPass            String token,String phone

"""

phone = "17761196077"
def token(phone):
    if phone == "15680785518":
        token = "2a7570e2fec348e1b91df961ccf8ee0e_app"
        familyPhone = "18683953197"
    elif phone == "17761196077":
        token = "1f7e0db62349483d9f0b43dbd6318985_app"
        familyPhone = "15566666661"
    else:
        token = None
        familyPhone = None
    return token,familyPhone

token,familyPhone = token(phone)

sendCode = requests.post(DATA.sendSecurityCode(),data={'phone':phone})
insertLog(sendCode.url,phone,sendCode.text)
assert True == sendCode.json()['success']  ## 验证码发送失败则不继续执行



securityCode = raw_input("securityCode:")
data = {"phone":phone,"token":token,"type":31}
data2 = {"phone":phone,"token":token,"oldPayPassword":"123456","newPayPassword":"111111"}
payValidate = {"phone":phone,"token":token,"payPassword":"123456"}
forgetPayPassword = {"phone":phone,"token":token,"securityCode":securityCode}
resetPayPassword = {"phone":phone,"token":token,"validateStr":"123456","payPassword":"123456"}
transdata = {"phone":phone,"token":token,"familyPhone":familyPhone,"transferAmount":1000,"payPwd":"123456"}

method = "forgetPayPassword"

result =  wallit(method,forgetPayPassword)

insertLog(method,forgetPayPassword,result.text)

