import sys, io

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
sys.path.append(str(BASE_DIR))

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="gb18030")

import orm.manage
import time

from Bili.daily.DailyTask import DailyTask
from Bili.db.models import ExpRecord
from Bili.live.BiLiveTask import BiLiveTask
from Bili.BilibliInfo import BilibliInfo
from Bili.util.Request import Request

SUCCESS = 0

Bili = BilibliInfo.get_instance()

today = time.strftime("%Y-%m-%d", time.localtime())
record = ExpRecord.objects.filter(record_date=today)


def check():
    url = "https://api.bilibili.com/x/web-interface/nav"
    r = Request()
    response = r.get(url)

    if not response:
        return False

    json_object = response.json()
    data_object = json_object.get("data")
    code = json_object.get("code")

    if code == SUCCESS:
        Bili.uname = data_object.get("uname")
        Bili.mid = data_object.get("mid")
        Bili.vipType = data_object.get("vipType")
        Bili.money = data_object.get("money")
        Bili.current_exp = data_object.get("level_info").get("current_exp")
        Bili.vipStatus = data_object.get("vipStatus")
        Bili.coupon_balance = data_object.get("wallet").get("coupon_balance")

        if record:
            return True

        try:
            ExpRecord.objects.create(uname=Bili.uname, uid=Bili.mid, current_exp=Bili.current_exp, coins=Bili.money)
        except Exception as e:
            print("已存在该记录")

        return True

    return False


def main():
    ret = check()
    if not ret:
        print(str(Bili.uname))
        print(str(Bili.mid))
        print(str(Bili.current_exp))

    daily_task = DailyTask()
    daily_task.run()

    if not record:
        daily_task.comic_sign()
        BiLiveTask().run()


if __name__ == '__main__':
    main()
