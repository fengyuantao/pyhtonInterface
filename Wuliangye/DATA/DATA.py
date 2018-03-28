#coding:utf-8
Interface = "http://192.168.2.240:9138/doc/"
Interface2 = "http://192.168.2.200:2223/index.html"
url_register = "http://192.168.2.240:9138/index.php/app/user/register"
def url_register():
    u"""APP注册接口"""
    url_register = "http://192.168.2.240:9138/index.php/app/user/register"
    return url_register
def url_login():
    u"""APP登录接口"""
    url_login = "http://192.168.2.240:9138/index.php/app/user/login"
    return url_login
pushMessage = "http://192.168.2.200:2223/pushMessage"
notReadMessageNum = "http://192.168.2.200:2223/notReadMessageNum"
getUserHotMessage = "http://192.168.2.200:2223/getUserHotMessage"

verson = "http://192.168.2.240:9138/index.php/app/user/version"

#sendCodeByBusness="http://192.168.2.240:9138/index.php/app/user/sendCodeByBusness"
def sendCodeByBusness():
    u"""短信验证码接口"""
    return "http://192.168.2.240:9138/index.php/app/user/sendCodeByBusness"

#获取第三方支付接口

GetOtherPay = "http://wuliangye.scshangtong.com/puhuihua/external/pay/paymentThirdOrder"
"""
    参数：String phone,
	  String token,
	 String orderNo,
	  Integer amount(微信或支付宝支付金额),
	  Integer payFlag(1-威富通  2-支付宝)
	  返回：
	  {"data":null,"error":"成功","errorCode":0,"success":true}
"""
def sendSecurityCode():
    u'''
    发送短信验证码
    String phone

    '''
    return "http://wuliangye.scshangtong.com/puhuihua/app/userInfo/sendSecurityCode"

def validateCode():

    u"""
    验证短信验证码
    String phone, String code

    """
    return "http://wuliangye.scshangtong.com/puhuihua/app/userInfo/validateCode"

def validateActiveCode():
    u"""
    验证激活码
    String phone, String activeCode, String validateStr

    """
    return "http://wuliangye.scshangtong.com/puhuihua/app/userInfo/validateActiveCode"

def register():
    u"""
    注册侧激活
    string phone,string activeCode,string validateStr,string terminal,Integer loginDevice
    """
    return "http://wuliangye.scshangtong.com/puhuihua/app/userInfo/register"

def login():
    u"""
    登录
    String phone,String securityCode,String terminal,Integer loginDevice

    """
    return "http://wuliangye.scshangtong.com/puhuihua/app/userInfo/login"

def validateToken():
    u"""
    token有效验证
    string phone,string token
    """

    return "http://wuliangye.scshangtong.com/puhuihua/app/userInfo/validateToken"

def userInfo():
    u"""
        用户信息
        String phone, String token


    """

    return "http://wuliangye.scshangtong.com/puhuihua/app/userInfo/userInfo"

def myFamily():
    u"""
    我的家属
    String token, String phone

    """
    return "http://wuliangye.scshangtong.com/puhuihua/app/userInfo/myFamily"

def modifyHeadImage():
    u"""
    修改头像
    String token, String phone
    file名称：headImageFile
    """
    return "http://wuliangye.scshangtong.com/puhuihua/app/userInfo/modifyHeadImage"

def wordsList():
    """
    String token, String phone, Integer pageNo

    """
    return "http://wuliangye.scshangtong.com/puhuihua/app/userInfo/wordsList"

def leaveWords():
    """
    String token, String phone,String content
    """
    return "http://wuliangye.scshangtong.com/puhuihua/app/userInfo/leaveWords"

class Information(object):
    url = "http://wuliangye.scshangtong.com/puhuihua/app/unionService/"
    def __init__(self):
        self.hostInfoChannel = self.url + "hostInfoChannel" ##热点资讯渠道列表

        self.hostInfoDetail = self.url + "hostInfoDetail" ## 热点资讯详情  Integer id

        self.hostInfoList = self.url + "hostInfoList"  ## 热点资讯列表 Integer channelId, Integer count

        self.activityChannel = self.url + "activityChannel" ## 活动渠道列表

        self.activityList = self.url + "activityList" ##活动列表  Integer pageNo, Integer channelType, Integer timeType

        self.activityDetail = self.url + "activityDetail"  ## 活动详情   Integer issueId

        self.activityApply = self.url + "activityApply" ##  活动报名信息提交 Integer issueId,String token,String phone,String details

        self.fetchActiveityField = self.url + "fetchActiveityField" ## 获取活动报名需填写字段   Integer issueId,String token,String phone

        self.dynamicInfoList = self.url + "dynamicInfoList" ##  动态资讯列表 Integer pageNo

        self.dynamicInfoDetail = self.url + "dynamicInfoDetail" ## 动态资讯详情 Integer id

        self.mutualList = self.url + "mutualList" ## 互助保障列表  Integer pageNo

        self.mutualDetail = self.url + "mutualDetail" ## 互助保障详情 Integer id

        self.promotionList = self.url + "promotionList" ## 素质提升列表  Integer pageNo

        self.promotionDetail = self.url + "promotionDetail"  ## 素质提升详情  Integer id

        self.legalList = self.url + "legalList" ## 法律服务列表  Integer pageNo

        self.legalDetail = self.url + "legalDetail" ## 法律服务详情  Integer id

        self.psychologyList = self.url + "psychologyList" ## 心理减压列表  Integer pageNo

        self.psychologyDetail = self.url + "psychologyDetail" ## 心理减压详情 Integer id

        self.povertyList = self.url + "povertyList" ## 精准扶贫列表  Integer pageNo

        self.povertyDetail = self.url + "povertyDetail" ## 精准扶贫详情 Integer id

        self.consultationList = self.url + "consultationList" ## 法律咨询列表 String phone, String token, Integer pageNo

        self.addConsultation = self.url + "addConsultation" ## 添加法律咨询 String phone, String token,String content

class Wallet(object):
    url = "http://wuliangye.scshangtong.com/puhuihua/app/wallet/"

    def __init__(self):
        self.hasPayPassword = self.url + "hasPayPassword" ## 验证是否有支付密码 String phone, String token

        self.setPayPassword = self.url + "setPayPassword" ##  设置支付密码   String phone,String token,String payPassword

        self.forgetPayPassword = self.url + "forgetPayPassword" ## 忘记支付密码  String phone,String token,String securityCode

        self.resetPayPassword = self.url + "resetPayPassword"  ## 重置支付密码 String token,String phone,String validateStr,String payPassword

        self.modifyPayPassword = self.url + "modifyPayPassword" ## 修改支付密码 String phone,String token,String oldPayPassword,String newPayPassword

        self.payValidate = self.url + "payValidate"  ## 验证支付密码 String token,String payPassword,String phone

        self.bindCard = self.url + "bindCard" ## 绑定银行卡  String token, BankCard bankCard,String securityCode,MultipartHttpServletRequest request,String phone

        self.getCardInfo = self.url + "getCardInfo" ## 获取银行卡信息 String token,String phone

        self.bindCardChange = self.url + "bindCardChange" ## 更改银行卡  String token, BankCard bankCard, String securityCode,String phone

        self.setNoPass = self.url + "setNoPass" ## 设置免密支付 String token,String phone,String payPassword,Integer noPass

        self.hasPass = self.url + "hasPass" ## 判断是否免密  String token,String phone

        self.codeCreate = self.url + "codeCreate" ## 获取条码付凭证  String token,String validateStr,String phone

        self.cardCodeCreate = self.url + "cardCodeCreate"  ## 获取银行卡付款凭证  String token,String validateStr,String phone

        self.codePayDetails = self.url + "codePayDetails" ## 条码支付情况   String token,Long timestamp,String phone

        self.unionList = self.url + "unionList" ## 获取工会组织列表 Integer pageSize, String name,Integer pageNo,String token,String phone


class indexInfo(object):
    url = "http://wuliangye.scshangtong.com/puhuihua/index/indexInfo/"
    def __init__(self):
        self.areaAndCircle = self.url + "areaAndCircle" ## 获取区域和商圈列表

        self.merchantType = self.url + "merchantType" ## 获取商户类型列表

        self.nearbyMerchantList = self.url + "nearbyMerchantList" ## 获取附近商家列表详情 Float lng, Float lat,Integer page, Integer areaId,Integer shoppingAreaId,Integer typeId,Integer istance

        self.getByMerchantId = self.url + "getByMerchantId" ## 商户详情 Float lng,Float lat,Integer merchantId

        self.conPaySwitch = self.url + "conPaySwitch" ## 便民缴费开关  String phone,String token, Integer code

        self.convenientPayment = self.url + "convenientPayment" ## 水电气费缴纳查询 String billKey,String token,String phone,String companyId

class message(object):
    url = "http://wuliangye.scshangtong.com/puhuihua/index/indexInfo/"
    def __init__(self):
        self.instationMsgList = self.url + "instationMsgList" ## 查询消息列表 String phone,String token,Integer type,Integer pageNo,Integer pageSize

        self.newFirstMsgList = self.url + "newFirstMsgList" ## 查询最新第一条信息  String phone, String token

        self.unreadMsgCount = self.url + "unreadMsgCount" ##未读消息统计

        self.updateInstationMsg = self.url+"updateInstationMsg" ## 修改消息  String phone, String token,Integer msgId,Integer readStatus

class payOrder(object):
    url = "http://wuliangye.scshangtong.com/puhuihua/external/pay/"
    def __init__(self):
        self.transferFamily = "http://wuliangye.scshangtong.com/puhuihua/app/userInfo/transferFamily" ## 向家属转账   String phone,String token,familyPhone,Integer transferAmount,String payPwd
        self.codeCreate = "http://wuliangye.scshangtong.com/puhuihua/app/wallet/codeCreate" #  二维码生成  String token,String phone,Integer type（31-和信通账户；33-银行卡）
        self.placeAnOrder = self.url + "placeAnOrder" ## 统一下单  String phone,String token,String channelNo,String merchantId,Integer amount,String callBack,String desc,Integer orderType（1-消费；2-充值）
        self.paymentOrder = self.url + "paymentOrder" ## 订单支付(账户余额、银行卡、专项资金)  String phone,String token,String payPwd,String orderNo,Integer payFlag(0-余额1-银行卡9-专项资金)
        self.hexinCardRecharge = self.url + "hexinCardRecharge" ## 和信通卡订单充值  String phone,String token,String orderNo,String cardNo,String cardPwd