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
data = Excel.ExcelRead(by_name=u'login')
thisData = data.excel_table_byname()
#thisData = [{"date":"1519895532","sid":"cfd6881d665496e1868ecf984ea324a","keycode":"219f09d055dd182746fcb813bfc928c0","results":{},"systemType":1},
#            {"date":"1519895532","sid":"cfd6881d665496e1868ecf984ea324ba","keycode":"219f09d055dd182746fcb813bfc928c0","results":{},"systemType":2}]

@ddt.ddt
class test_AppInterface(unittest.TestCase):
    def setUp(self):
        self.login = DATA.login()
        self.sendCodeUrl = DATA.sendSecurityCode()
        self.validateCode = DATA.validateCode()

    @ddt.data(*thisData)
    def test_login(self,Data):


        Expected_results = Data.pop("ExpectedResults")

        result = requests.post(self.login,data=Data)
        print  self.login + " : "+result._content
        self.assertEqual(Expected_results,result.ok,msg=result.ok)

    def test_sendSecurityCode(self):
        data = {"phone":"15680785518"}
        result = requests.post(self.sendCodeUrl,data=data)
        print self.sendCodeUrl + " : "+result._content
        code = "123454"
        put_data = {"phone":"15680785518","code":code}
        res = requests.post(self.validateCode,data = put_data)
        print self.validateCode + " : " + res._content

    def tearDown(self):
        pass

