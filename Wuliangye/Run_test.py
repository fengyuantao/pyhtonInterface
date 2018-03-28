#coding:utf-8
from Email_get_Report import Send_Email
from Email_get_Report import GetReport
import unittest,time,HTMLTestRunner

def send_mail():
    report_file = GetReport.getReport()
    sender = ['815060224@qq.com','fengyuantao@hexinpass.com']
    #sender=[]
    mail = Send_Email.Email(report_file,sender,u'自动化测试报告',u'过奖了哈')
    result = mail.Send()
    if result:
        print u"邮件发送成功"
    else:
        print u"邮件发送失败"
def create_suite():
    base_dire = "E:\\pyFile\\Wuliangye\\test_case"
    testunite = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(base_dire,
                                                   pattern='test_*.py',
                                                   top_level_dir=None)
    for test in discover:
        for case in test:
            testunite.addTest(case)
    return testunite
if __name__ == '__main__':
    all_case = create_suite()
    now_time = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())
    filename = 'E:\\pyFile\\Wuliangye\\report\\'+now_time+'AutoTest_Report.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'文化厅接口测试自动化',description=u'用例执行结果：')
    runner.run(all_case)
    fp.close()
    time.sleep(1)
    send_mail()