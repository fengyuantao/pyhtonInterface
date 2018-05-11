#coding:utf-8
import MySQLdb

import sys
reload(sys)
sys.setdefaultencoding('utf8')

#打开数据库
class Conect(object):
    def __init__(self):
        self.db = MySQLdb.connect(host="localhost",
                                  port=3306,
                                  user='root',
                                  passwd='123456',
                                  db='wuliangye',
                                  charset='utf8'
                        )
        self.cur = self.db.cursor()

    def find_data(self,colon,table,id=None):
        if table == 'idcard':
            sql = "select {0} from {1};".format(colon,table)
        elif table == 'username':
            sql = "select {0} from {1};".format(colon,table)
        else:
            sql = "select {0} from {1} where {0}={2};".format(colon,table,id)
        #print sql
        self.cur.execute(sql)
        data = self.cur.fetchall()
        #self.cur.close()
        self.db.commit()
        #self.db.close()
        return data

    def insert_data(self,table,name=None,idcard=None,phone=None,Intime=None,wechat=None,address=None,birthday=None,gender=None):
        if table == 'idcard':
            sql = "insert into {0} values({1});".format(table,idcard)
        elif table == 'username':
            sql = "insert into username(idcarduser,username,userphone,Intime,wechat,address) values('{0}','{1}','{2}','{3}','{4}','{5}');".format(idcard,name,phone,Intime,wechat,address)
        else:
            sql = "insert into familyinfo values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}');".format(idcard,name,phone,Intime,wechat,address,birthday,gender)
        #print sql
        #print sql1.format(acture_p,is_pass,id)
        self.cur.execute(sql)
        self.db.commit()
        #self.db.close()

