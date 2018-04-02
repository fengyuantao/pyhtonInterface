#coding:utf-8
import xlrd
import xlwt
from xlutils.copy import copy
import IDcard,random
from collections import OrderedDict
 #根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
class ExcelRead(object):
    def __init__(self,file= 'E:\\gitRepositoy\\\importMessages\\messageUser.xls',colnameindex=0,by_name=u'Sheet1'):
        self.file = file
        self.colnameindex = colnameindex
        self.by_name = by_name
        self.flag = None
    def excel_table_byname(self):
        try:
            data = xlrd.open_workbook(self.file)
            table = data.sheet_by_name(self.by_name)
            nrows = table.nrows #行数
            colnames =  table.row_values(self.colnameindex) #某一行数据
            list =[]
            for rownum in range(1,nrows):
                row = table.row_values(rownum)
                if row:
                    app = {}
                    for i in range(len(colnames)):
                        app[colnames[i]] = row[i]
                    list.append(app)
            return list
        except BaseException,e:
            return e.message
    def write_to_excel(self,**kwargs):

        try:
            rexcel = xlrd.open_workbook(self.file) # 用wlrd提供的方法读取一个excel文件
            rows = rexcel.sheet_by_name(self.by_name).nrows# 用wlrd提供的方法获得现在已有的行数
            clons = rexcel.sheet_by_name(self.by_name).row_values(self.colnameindex) # 获取总共有几列数据
            excel = copy(rexcel)  # 用xlutils提供的copy方法将xlrd的对象转化为xlwt的对象
            table = excel.get_sheet(self.by_name)

            clon = 0
            for key in kwargs:
                print key
                table.write(rows,clon,kwargs[key])
                clon += 1
            '''
                table.write(rows,0,kwargs['phone'])
                table.write(rows,1,kwargs['token'])
             '''
            excel.save(self.file)# xlwt对象的保存方法，这时便覆盖掉了原来的excel
            self.flag = u"表{}数据更新成功".format(table)
        except BaseException,e:
            self.flag = e
        finally:
            return self.flag


def insert():

    idcard = IDcard.getcode()
    name1 = list("abcdefghijklmnopqrstuvwxyz0123456789")
    num = random.randint(1,9)
    name = random.choice(name1) * num
    year = random.randint(1970,2018)
    moth = random.choice(['01','02','03','04','05','06','07','08','09','10','11','12'])
    day = random.choice(['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','21','22','23','24','25','26','27','28'])
    Intime = str(year) + moth + day
    wechat = Intime
    address = random.choice(name1) * (num+5)
    nation = random.choice([u'汉族',u'壮族',u'回族',u'维吾尔族',u'苗族'])
    basicunion = random.choice([u'机关一分会',u'机关二分会',u'机关三分会',u'机关四分会',u'机关五分会',u'机关六分会',u'501车间分会',u'502车间分会',u'503车间分会',u'504车间分会'])
    depatment = random.choice(['ddddd',u'抖音','qweqwe'])
    degree = random.choice([u'博士',u'硕士',u'本科',u'硕士',u'大专',u'小学以下',u'初中'])
    Political = random.choice([u'中共党员',u'群众'u'中共预备党员'u'共青团员'])
    isdifficulty = random.choice([u'是',u'否'])
    iscountryside = random.choice([u'是',u'否'])
    birthday = idcard[7:14]

    phone = random.choice(['131','132','133','134','135','136','137','156','187','177']) + Intime
    if int(idcard[-2]) % 2 == 1:
        gender = u'男'
    else:
        gender = u'女'
    jobstatus = random.choice([u'在职',u'离职',u'退休',u'休假',u'其它'])
    data = {"name":name,"idcard":idcard,'phone':phone,'Intime':Intime,'wechat':wechat,'address':address,'nation':nation,'basicunion':basicunion,'depatment':depatment,'degree':degree,
        'Political':Political,'isdifficulty':isdifficulty,'iscountryside':iscountryside,'birthday':birthday,'gender':gender,'jobstatus':jobstatus}

    return data


data = insert()
print data
L = ExcelRead()
message = L.write_to_excel(**data)
print message


