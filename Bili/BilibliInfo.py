import configparser
import json

import orm.manage
from Bili.db.models import Cookies


class BilibliInfo:
    Bili = None

    def __init__(self):
        self.sessdata = None
        self.bili_jct = None
        self.dedeuserid = None
        self.buvid3 = None
        # 用户名
        self.uname = None
        # uid
        self.mid = None
        # vip 类型
        self.vipType = None
        # 硬币
        self.money = None
        # 当前经验
        self.current_exp = None
        # 大会员状态
        self.vipStatus = None
        # B币券余额
        self.coupon_balance = None

    def set_cookies(self, sessdata, bili_jct, dedeuserid, buvid3):
        self.sessdata = sessdata
        self.bili_jct = bili_jct
        self.dedeuserid = dedeuserid
        self.buvid3 = buvid3

    def init(self):
        cookie = Cookies.objects.filter(state=0, website="bilibili").first()
        if not cookie:
            exit()

        cookie_dict = json.loads(cookie.cookie_value)

        # 读取properties文件中的值
        sessdata = cookie_dict.get('SESSDATA')
        bili_jct = cookie_dict.get('bili_jct')
        dedeuserid = cookie_dict.get('DedeUserID')
        buvid3 = cookie_dict.get('buvid3')

        self.set_cookies(sessdata, bili_jct, dedeuserid, buvid3)

    def get_cookies(self):
        return "SESSDATA={};bili_jct={};DedeUserID={};buvid3={}" \
            .format(self.sessdata, self.bili_jct, self.dedeuserid, self.buvid3) \
            .replace("'", "")

    @classmethod
    def get_instance(cls):
        if not cls.Bili:
            cls.Bili = cls()
            cls.Bili.init()

        return cls.Bili
