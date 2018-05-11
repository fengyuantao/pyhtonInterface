#coding:utf-8
import xlrd
import xlwt
from xlutils.copy import copy
import IDcard,random
from collections import OrderedDict
from ConnectSQL import Conect
import sys
reload(sys)
sys.setdefaultencoding('utf8')
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
    def write_to_excel(self,kwargs):

        try:
            rexcel = xlrd.open_workbook(self.file) # 用wlrd提供的方法读取一个excel文件
            rows = rexcel.sheet_by_name(self.by_name).nrows# 用wlrd提供的方法获得现在已有的行数
            clons = rexcel.sheet_by_name(self.by_name).row_values(self.colnameindex) # 获取总共有几列数据
            excel = copy(rexcel)  # 用xlutils提供的copy方法将xlrd的对象转化为xlwt的对象
            table = excel.get_sheet(self.by_name)

            clon = 0
            for key in kwargs:

                table.write(rows,clon,key)
                clon += 1
            '''
                table.write(rows,0,kwargs['phone'])
                table.write(rows,1,kwargs['token'])
             '''
            excel.save(self.file)# xlwt对象的保存方法，这时便覆盖掉了原来的excel
            self.flag = True
        except BaseException,e:
            self.flag = e
        finally:
            return self.flag


def insert():
    sql = Conect()
    idcard = IDcard.getcode()
    name1 = list("abcdefghijklmnopqrstuvwxyz")
    chinaName = [u'张',u'王',u'宋',u'冯',u'李',u'刘',u'牛',u'吴',u'巨',u'费',u'东方',u'西方',u'北方',u'南方',u'巧',u'孔',u'孙',u'陈']
    num = list(u'甲乙丙丁吴挤更新电池貂蝉机关四分会傻逼啊要后端少女时代可能付款德生科技撒的发快递男生发康靖呢时点击好的撒回家你查四川科技你的会计师成本价哈斯巴达时间内擦擦擦地上')
    name =random.choice(chinaName)  + random.choice(num)+ random.choice(name1)
    year = random.randint(1970,2018)
    moth = random.choice(['01','02','03','04','05','06','07','08','09','10','11','12'])
    day = random.choice(['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','21','22','23','24','25','26','27','28'])
    Intime = str(year) + moth + day
    wechat = Intime
    address = random.choice(name1) + (name+name)

    nation = random.choice([u'汉族',u'壮族',u'回族',u'维吾尔族',u'苗族'])
    basicunion = random.choice([u'财务公司分会',u'机关二分会',u'机关三分会',u'机关四分会',u'机关五分会',u'机关六分会',u'501车间分会',u'502车间分会',u'503车间分会',u'504车间分会',u'安监部分会',u'职工服务中心分会'])
    depatment = random.choice(['ddddd',u'抖音','qweqwe'])
    degree = random.choice([u'博士',u'硕士',u'本科',u'硕士',u'大专',u'小学以下',u'初中'])
    Political = random.choice([u'中共党员',u'群众',u'中共预备党员',u'共青团员'])
    isdifficulty = random.choice([u'是',u'否'])
    iscountryside = random.choice([u'是',u'否'])



    phone = random.choice(['131','132','133','134','135','136','137','156','187','177']) + Intime
    phon3 = '18607732201' ## 空号

    jobstatus = random.choice([u'在职',u'离职',u'退休',u'休假',u'其它'])
    '''
    data = {"name":name,"idcard":idcard,'phone':phone,'Intime':Intime,'wechat':wechat,'address':address,'nation':nation,'basicunion':basicunion,'depatment':depatment,'degree':degree,
        'Political':Political,'isdifficulty':isdifficulty,'iscountryside':iscountryside,'birthday':birthday,'gender':gender,'jobstatus':jobstatus}
    '''
    data =[name,idcard,phone,Intime,wechat,address,nation,basicunion,depatment,degree,
           Political,isdifficulty,iscountryside,jobstatus]
    sql.insert_data('username',name,idcard,phone,Intime,wechat,address,birthday=None,gender=None)

    return data
def insertFamily():
    sql = Conect()
    idcard = IDcard.getcode()
    name1 = list(u"都不说话北方导航基本上补卡王不记得不刷卡机冯大把时间能抵扣巴不得科技部副科级啊速度快不菲的南水北调就gdsafvgdafsd")
    chinaName = [u'张',u'王',u'宋',u'冯',u'李',u'刘',u'牛',u'吴',u'巨',u'费',u'东方',u'西方',u'北方',u'南方',u'巧',u'孔',u'孙',u'陈']
    num = random.randint(1,9)
    name =random.choice(chinaName) + random.choice(name1) + str(num * 11)
    phone = random.choice(['131','132','133','134','135','136','137','156','187','177']) + str(random.randint(1000,9999)) +str(random.randint(1000,9999))
    usercrad = sql.find_data('*','username')
    relation = random.choice(usercrad)

    relationName = relation[0]
    relationIdcard = relation[1]
    #relationship = random.choice([u'配偶',u'父子',u'父女',u'母子',u'母女'])

    if int(idcard[-2]) % 2 == 1:

        if int(relationIdcard[-1]) ==1:
            relationship = random.choice([u'父子',u'母子'])
        else:
            relationship = random.choice([u'父女',u'母子',u'配偶'])
    else:

        if int(relationIdcard[-1]) ==1:
            relationship = random.choice([u'父女',u'母子',u'配偶'])
        else:
            relationship = random.choice([u'父子',u'母子'])

    data = [name,idcard,phone,relationName,relationIdcard,relationship]
    sql.insert_data('familyinfo',name=name,idcard=idcard,phone=phone,Intime=relationName,wechat=relationIdcard,address=relationship,birthday=None,gender=None)

    return data
import time
import threading
lock = threading.Lock()
def createDate(i):

    lock.acquire()

    data = insert()

    L = ExcelRead()

    message = L.write_to_excel(data)

    if message:
        print u'第{}条数据更新成功！'.format(i)

    lock.release()






threads = []



if __name__ == '__main__':
    for i in range(9000):
        thread1 = threading.Thread(target=createDate,args=(i,))
        threads.append(thread1)
        thread1.start()
    for thread in threads:
        thread.join()









