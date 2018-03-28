#coding:utf-8
import MySQLdb
import sys

import sudsA
#打开数据库
class Conect(object):
    def __init__(self):
        self.db = MySQLdb.connect(host="localhost",
                                  port=3306,
                                  user='root',
                                  passwd='123456',
                                  db='auto_test',
                                  charset='utf8'
                        )
        self.cur = self.db.cursor()

    def find_data(self,table,id):
        if table == 'test_case_ctqy':
            sql1 = "select cardNO,dateFrom,dateTo,isPager,merchantNo,pageNo,pageSize,queryType,userId,pre_p from {} where id={}"
        elif table == 'test_case_IdadBillBean':
            sql1 = "select amount,billNo,carNo,merchantNo,terminal,txndate,txntime,useId,isVerifyPassword,password from {} where id={}"
        elif table == 'test_case_iprf':
            sql1 = "select amount,carNo,merchantNo,txnId,useId from {} where id={}"
        elif table == 'test_infoByAll':
            sql1 = "select cardNo,isVerifyPassword,merchantNo,userId,password from {} where id={}"
        elif table == 'test_case_islvBy':
            sql1 = "select amount,buyPerson,cardNoFrom,cardNoTo,discount,expiredDate,merchantNo,serialNo,totalAmount,userId from {} where id={}"
        elif table=='test_case_idvvBy':
            sql1 = "select DMerchantNo,amount,cardNoFrom,cardNoTo,merchantNo,serialNo,totalAmount,userId from {} where id={}"
        elif table=="test_case_stat":
            sql1 = "select cardNoFrom,cardNoTo,merchantNo,type,userId from {} where id={}"
        elif table=='test_case_itrf':
            sql1 = "select amount,cardNoFrom,cardNoTo,merchantNo,password,userId,needPwd from {} where id={}"
        elif table == 'test_case_batchPostpone':
            sql1 = "select cardNoFrom,cardNoTo,merchantNo,reqExpireDate,userId from {} where id={}"
        elif table=='test_case_rstpt':
            sql1="select cardNo,merchantNo,userId from {} where id={}"
        elif table=="test_case_ictv":
            sql1 = "select cardNoFrom,cardNoTo,merchantNo,password,userId from {} where id={}"
        elif table=="test_case_updp":
            sql1 = "select cardNo,merchantNo,newPassword,oldPassword,userId from {} where id={}"
        else:
            sql1 =None
        self.cur.execute(sql1.format(table,id))
        data = self.cur.fetchone()
        #self.cur.close()
        self.db.commit()
        #self.db.close()
        return data
    def update_data(self,table,pre,acture_p,is_pass,case_name,id,txnid=None):
        if txnid is None:
            sql1 = "update {} set pre_p='{}',acture_p='{}',is_pass={},case_name='{}' where id={}"
            #print sql1.format(acture_p,is_pass,id)
            self.cur.execute(sql1.format(table,pre,acture_p,is_pass,case_name,id))
            self.db.commit()
            #self.db.close()
        else:
            if table == 'test_case_IdadBillBean':
                sql1 = "update {} set pre_p='{}',acture_p='{}',is_pass={},case_name='{}' where id={}"
                sql2 = "update test_case_iprf set txnId='{}' where id<10"
                try:
                    self.cur.execute(sql1.format(table,pre,acture_p,is_pass,case_name,id))
                    self.cur.execute(sql2.format(txnid))
                    self.db.commit()
                except Exception,e:
                    print e



c,data = sudsA.BBBB('ns3:UpdpBean')
d = Conect().find_data('test_case_updp',1)
data.cardNo = '8333028011236656379'
data.merchantNo = '510990120400175'
data.newPassword = '111111'
data.oldPassword='002556'
data.userId='1eww'
res = c.service['imTxnServiceHttpEndpoint'].updp(data)
print res
'''
cc,ddata = sudsA.BBBB('ns3:IdadBill4BYJKBean')
dd = Conect().find_data('test_case_IdadBillBean',1)
ddata.amount=dd[0]
ddata.billNo=dd[1]
ddata.cardNo =dd[2]
ddata.merchantNo=dd[3]
ddata.terminal =dd[4]
ddata.txndate=dd[5]
ddata.txntime=dd[6]
ddata.userId=dd[7]
ddata.isVerifyPassword = dd[8]
ddata.password = dd[9]
print ddata
res1 = cc.service['imTxnServiceHttpEndpoint'].idadWithBill4BYJK(ddata)
print res1
Conect().update_data('test_case_IdadBillBean','PZ','PZ',1,'yes',1,txnid=res1[6])
print res1[6]


c,data = sudsA.BBBB('ns3:IprfBean')

print data

d = Conect().find_data('test_case_iprf',1)
print d
data.amount=d[0]
data.cardNo =d[1]
data.merchantNo=d[2]
data.txnId=d[3]
data.userId=d[4]
print data
res = c.service['imTxnServiceHttpEndpoint'].iprf(data)
print type(res[0])
#print res[6]
#p = Conect().update_data('test_case_IdadBillBean','pz','pz',1,'no',1,txnid=res[6])

'''