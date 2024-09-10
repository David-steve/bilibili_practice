import orm.manage
import time

from Bili.daily.DailyTask import DailyTask
from Bili.db.models import ExpRecord
from Bili.live.BiLiveTask import BiLiveTask
from Bili.BilibliInfo import BilibliInfo
from Bili.util.Request import Request

SUCCESS = 0

bili = BilibliInfo.get_instance()

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
        bili.uname = data_object.get("uname")
        bili.mid = data_object.get("mid")
        bili.vipType = data_object.get("vipType")
        bili.money = data_object.get("money")
        bili.current_exp = data_object.get("level_info").get("current_exp")
        bili.vipStatus = data_object.get("vipStatus")
        bili.coupon_balance = data_object.get("wallet").get("coupon_balance")

        if record:
            return True

        try:
            ExpRecord.objects.create(uname=bili.uname, uid=bili.mid, current_exp=bili.current_exp, coins=bili.money)
        except Exception as e:
            print("已存在该记录", e)

        return True

    return False


def main():
    ret = check()
    if ret:
        print(str(bili.uname))
        print(str(bili.mid))
        print(str(bili.current_exp))
    else:
        raise ValueError("cookies 过期")

    daily_task = DailyTask(bili)
    daily_task.run()

    if not record:
        daily_task.comic_sign()
        BiLiveTask().run()


if __name__ == '__main__':
    main()
