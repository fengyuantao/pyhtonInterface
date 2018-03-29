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

class Information(unittest.TestCase):
    def setUp(self):
        self.url = DATA.Information()
        self.num = 50

    def test_01_hostInfoChannel(self):
        url = DATA.Information()
        result = requests.get(url.hostInfoChannel)
        print result.url
        print "hostInfoChannel:" + result._content
        print "*"* self.num
        res = result.json()["data"]
        channelId = res[2]['channelId']
        parms = {"channelId":channelId,"count":10}
        res_hostInfoList = requests.get(url.hostInfoList,params=parms)
        print res_hostInfoList.url
        print "hostInfoList:" + res_hostInfoList._content
        print "*"* self.num
        parms_hostInfoDetail = {"id":2}
        res_hostInfoDetail = requests.get(url.hostInfoDetail,params=parms_hostInfoDetail)
        print res_hostInfoDetail.url
        print "hostInfoDetail:" + res_hostInfoDetail._content
        print "*"* self.num

    def test_02_activity(self):
        print "get activityChannel:"
        result = requests.get(self.url.activityChannel)
        print result._content
        print "*"* self.num
        if result.json()["success"]:
            parms = {'pageNo':1,'channelType':10,'timeType':1}
            print 'get activityList:'
            result = requests.get(self.url.activityList,params=parms)
            print result._content
            print "*"* self.num
            if result.json()["data"] is not None:
                print "get activityDetail:"
                parms = {'issueId':result.json()['data'][0]['issueId']}
                result = requests.get(self.url.activityDetail,params=parms)
                print result._content
                print "*"* self.num

        listpaID = ['dynamicInfoList','mutualList','promotionList','legalList','psychologyList','consultationList']
        parms_listpageNo = {"pageNo":1}
        parms_ID= {"id":1}

        thisList = ['__class__', '__delattr__', '__dict__', '__doc__', '__format__',
                    '__getattribute__', '__hash__', '__init__', '__module__', '__new__',
                    '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
                    '__str__', '__subclasshook__', '__weakref__', 'activityApply', 'activityChannel'
            , 'activityDetail', 'activityList','hostInfoChannel','hostInfoList','hostInfoDetail','url',
                    'dynamicInfoList','mutualList','promotionList','legalList','psychologyList','fetchActiveityField'
                    ,"consultationList",'povertyList','povertyDetail']

        listpageNo = [i for i in dir(self.url) if i not in thisList]
        res_dict = {}
        for pageNo in listpaID:
            print "get {}:".format(pageNo)
            if pageNo == 'consultationList':
                result = requests.post(self.url.__dict__[pageNo],data={'phone':'17761196077','token':'1f7e0db62349483d9f0b43dbd6318985_app','pageNo':1})
            else:
                result = requests.get(self.url.__dict__[pageNo],params=parms_listpageNo)
                res_dict[pageNo[:4]] = result.json()["data"][0]["issueId"]
            print result._content
            print "*"* self.num
        print res_dict

        for pageNo in  listpageNo:
            print "get {}:".format(pageNo)
            if pageNo == 'addConsultation':
                result = requests.post(self.url.__dict__[pageNo],data={'phone':'17761196077','token':'1f7e0db62349483d9f0b43dbd6318985_app','content':'today we will test this function:{}'.format(time.asctime())})
            else:
                parms_ID["id"] = res_dict[pageNo[:4]]
                result = requests.get(self.url.__dict__[pageNo],params=parms_ID)
            print result._content
            print "*"* self.num

    def tearDown(self):
        pass