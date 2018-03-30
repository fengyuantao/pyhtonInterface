#coding:utf-8
import logging
def log():
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.INFO)
    handler = logging.FileHandler("../DATA/log.txt")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)

    logger.addHandler(handler)
    logger.addHandler(console)
    return logger
log = log()

def insertLog(method,data,result):

    log.info("****************************************************************************************************")
    log.info(u"接口请求地址 Test Interface:{}".format(method) )
    log.info(u"传入参数 Insert Data:{}".format(data))
    log.info(u"返回数据 Return Data:{}".format(result))