#coding:utf-8
import xlrd
import xlwt
from xlutils.copy import copy

 #根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
class ExcelRead(object):
    def __init__(self,file= 'E:\\pyFile\\Wuliangye\\DATA\\newdata1.xls',colnameindex=0,by_name=u'Sheet1'):
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
                table.write(rows,clon,kwargs[key])
                clon += 1
            '''
                table.write(rows,0,kwargs['phone'])
                table.write(rows,1,kwargs['token'])
             '''
            excel.save(self.file)# xlwt对象的保存方法，这时便覆盖掉了原来的excel
            self.flag = u"表{}数据更新成功".format(table)
        except BaseException,e:
                self.flag = e.message
        finally:
            return self.flag




