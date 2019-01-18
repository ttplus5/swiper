'''业务配置以及第三方平台的配置'''

REWIND_TIMES = 3 # 每日反悔次数

#滑动积分的配置
SCORE_LIKE = 5 #右滑积分
SCORE_DISLIKE = -5 #左滑积分
SCORE_SUPERLIKE = 7 #上滑积分


# 云之讯短信平台配置
YZX_SMS_API = 'https://open.ucpaas.com/ol/sms/sendsms'
YZX_SMS_PARAMS = {
    "sid": '5c6494b8c4a05b13e4950d4fcc9f49b3',
    "token": '0003c03249202dedb99cd38ceca6bc0b',
    "appid": 'f783770ec2fc4483bf77c29ddd0cc947',
    "templateid": "422457",
    "param": None,
    "mobile": None,
}


# 七牛云配置
QN_URL_PREFIX = 'http://pld16xicl.bkt.clouddn.com'
QN_ACCESS_KEY = 'eyW38sH1QyyCIrcCfIGejoMEIBbHhvSUnb7P5ODs'
QN_SECRET_KEY = 'nnEvVF-XNRJ_wBLZrPvChFQIHKlk5x5umV9CJhi0'
QN_BUCKET = 'bj1813'
