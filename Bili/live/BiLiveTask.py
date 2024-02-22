from time import sleep

from Bili.Task import Task
from Bili.util.Request import Request


class BiLiveTask(Task):
    def run(self):
        try:
            response = self.xlive_sign()
            json_obj = response.json()
            if json_obj.get('code') == self.SUCCESS:
                msg = "获得" + json_obj.get("data").get("text")
            else:
                msg = json_obj.get("message")

            print(f"直播签到--{msg}")
            sleep(5)
        except Exception as e:
            print(e)

    def xlive_sign(self):
        return Request.get("https://api.live.bilibili.com/xlive/web-ucenter/v1/sign/DoSign")