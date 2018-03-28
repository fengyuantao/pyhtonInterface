#coding:utf-8
import os

def getReport():
    base_dir = "E:\\pyFile\\Wuliangye\\report"
    list_file = os.listdir(base_dir)
    list_file.sort(key=lambda fn: os.path.getmtime(base_dir+"\\"+fn) if not
           os.path.isdir(base_dir+"\\"+fn) else 0)
    file = os.path.join(base_dir,list_file[-1])
    return file
'''
从测试报告中找到最近的文件，指定给file返回文件
'''