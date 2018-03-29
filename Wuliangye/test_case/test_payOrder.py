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

def transfer(method,data):
    url = DATA.payOrder()

    result = requests.post(url.__dict__[method],data)
    return result

def wallit(method,data):
    url = DATA.Wallet()
    result = requests.post(url.__dict__[method],data)
    return result
'''
setPayPassword_data = {"phone":"17761196077","token":"1f7e0db62349483d9f0b43dbd6318985_app","payPassword":"12346"}
method = "setPayPassword"
print wallit(method,setPayPassword_data)._content
'''

'''
data = {"phone":"17761196077","token":"1f7e0db62349483d9f0b43dbd6318985_app","familyPhone":"15680785518","transferAmount":100,"payPwd":"123456"}
method = "transferFamily"
print transfer(method,data)._content
'''

codeCreate_data = {"phone":"17761196077","token":"1f7e0db62349483d9f0b43dbd6318985_app","type":31}
codeCreate = "codeCreate"
print transfer(codeCreate,codeCreate_data)._content

