#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from suds.client import Client
import random,time,json,re
from suds.wsse import *

from suds.plugin import MessagePlugin
'''
封装suds，BBBB（）方法返回加入时间和用户名、密码后的Client
返回client和需要方法的data

'''
class MyPlugin(MessagePlugin):
    def received(self, context):
        reply_new=re.findall("<soap:Envelope.+</soap:Envelope>",context.reply,re.DOTALL)[0]
        context.reply=reply_new

    def BBBB(get_methot):
        url2 = 'http://192.168.2.107:9180/ppcmInterface/services/imTxnService?wsdl'
        url ='http://192.168.2.107:16080/frontsale/services/frontSaleQuotaManager?wsdl'
#logging.basicConfig(level=logging.INFO)
#logging.getLogger('suds.client').setLevel(logging.DEBUG)#加入日志
        c = Client(url2,plugins=[MyPlugin()])
        security = Security()
        token = UsernameToken('hxtWbsvSelfCinf','UbisMI')
        token1 = Timestamp()
        security.tokens.append(token1)
        security.tokens.append(token)
        c.set_options(wsse=security)
        data = c.factory.create(get_methot)
        return c,data



