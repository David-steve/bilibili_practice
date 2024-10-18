import orm.manage
from time import sleep

import requests

from Bili.db.models import Cookies
from common.Task import Task

cookie = Cookies.objects.filter(website='great_wall', user_id='david').first()
headers = eval(cookie.cookie_value)


class GreatWallTask(Task):
    @staticmethod
    def sign():
        url = "https://fintechappdr.cgws.com/api/business-credit-mall/h5/checkin/check"

        payload = {"data": ""}
        # headers = dict(cookie.cookie_value)

        response = requests.request("POST", url, json=payload, headers=headers)

        print(response.text)

    @staticmethod
    def do_daily_task():
        url = "https://fintechappdr.cgws.com/api/business-credit-mall/app/report/send"
        tasks = ["dailyReadingInformation", "dailyShareInformation"]

        # headers = cookie.cookie_value

        for task in tasks:
            payload = {"data": {"key": f"cgws://ljs/app/home/task/{task}"}}
            response = requests.request("POST", url, json=payload, headers=headers)
            print(response.text)

    def run(self):
        self.sign()

        for i in range(3):
            sleep(1)
            self.do_daily_task()


if __name__ == '__main__':
    GreatWallTask().run()
