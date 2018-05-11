
#coding:utf-8
import time
import random
from ConnectSQL import Conect

address = [110100,110101,110102,110103,110104,110105,110106,110107,110108,130701,130702,130703,130704,
           140401,140402,140421,140424,310100,310101,310102,310103,310104,310105,310106,310107,310108,
           510101,510104,510105,510106,510108,510112,511501,511502,511521,511522,511523,511524,511525,
           511526,511527,511529,511528,210283,210300,220322,220323,220381,220400,220402,220403,220421,
           220422,220500,220502,220503,220521,220523,22058,410724,410725,410727,410728,410781,410782]

SY = {0:"1",1:"0",2:"X",3:"9",4:"8",5:"7",6:"6",7:"5",8:"4",9:"3",10:"2"}

def getcode(m=None,d=None):
    SQL = Conect()
    year = random.randint(1970,2018)
    moth = random.choice(['01','02','03','04','05','06','07','08','09','10','11','12'])
    day = random.choice(['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','21','22','23','24','25','26','27','28'])
    add = random.choice(address)
    num = random.randint(100,999)
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2] # quan
    count = 0
    i = 0
    if m == None and d == None:
        perNum = str(add) + str(year) + moth + day +str(num)
    else:
        perNum = str(add) + str(year) + str(m)+ str(d) +str(num)
    for num in perNum:
        count +=  int(num) * weight[i]
        i +=1
    idcard = perNum + SY[count % 11] #jiao yan ma
    #fileName = open('IdCard.txt','rb')
    sqldata = SQL.find_data('idcard','idcard')

    if idcard in sqldata:
        return getcode()
    try:
        SQL.insert_data('idcard',idcard=idcard)
    except Exception:
        return getcode()

    '''

    for line in fileName.readlines():
        if idcard == line:
            return getcode()
    fileName.close()
    writeName = open('IdCard.txt','a')
    writeName.write(idcard + '\n')
    writeName.close()
    '''
    return idcard
'''
mycard = getcode('05','10')
print mycard
'''
