from time import sleep

import requests

from common.Task import Task


class GreatWallTask(Task):
    @staticmethod
    def sign():
        url = "https://fintechappdr.cgws.com/api/business-credit-mall/h5/checkin/check"

        payload = {"data": ""}
        headers = {
            "Host": "fintechappdr.cgws.com",
            "Content-Length": "11",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Accept": "application/json, text/plain, */*",
            "Timestamp": "1728301131446",
            "Signature": "645a9e57a52e9940af87e8769d8c8af298f9bd4b",
            "nonce": '929224',
            "Sessionid": "eb2cab58-f6e4-43ef-b8f4-c5b5c4c50ce6",
            "User-Agent": "Mozilla/5.0 (Linux; Android 12; PEEM00 Build/RKQ1.211103.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046285 Mobile Safari/537.36CustomUserAgent_C_4.15.0_Android elderMode_0",
            "Content-Type": "application/json;charset=UTF-8",
            "Origin": "https://fintechappdr.cgws.com",
            "X-Requested-With": "com.cgws.wealth",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://fintechappdr.cgws.com/oss-points-mall/h5/",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            # "Cookie": 'sensorsdata2015jssdkcross={"distinct_id":"191e4c406022a-0e6be360920756-95e6a2d-289440-191e4c406031b","first_id":"","props":{"$latest_traffic_source_type":"直接流量","$latest_search_keyword":"未取到值_直接打开","$latest_referrer":""},"$device_id":"191e4c406022a-0e6be360920756-95e6a2d-289440-191e4c406031b"}',
            "content-type": "application/json"
        }

        response = requests.request("POST", url, json=payload, headers=headers)

        print(response.text)

    @staticmethod
    def do_daily_task():
        url = "https://fintechappdr.cgws.com/api/business-credit-mall/app/report/send"
        tasks = ["dailyReadingInformation", "dailyShareInformation"]

        headers = {
            "Host": "fintechappdr.cgws.com",
            "content-length": "67",
            "pragma": "no-cache",
            "cache-control": "no-cache",
            "deviceid": "6f321a4a2f887c1c",
            "nonce": '783319',
            "phone": "18776666967",
            "user-agent": "Mozilla/5.0 (Linux; Android 12; PEEM00 Build/RKQ1.211103.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046285 Mobile Safari/537.36CustomUserAgent_C_4.15.0_Android elderMode_0",
            "content-type": "application/json; charset=UTF-8",
            "sessionid": "eb2cab58-f6e4-43ef-b8f4-c5b5c4c50ce6",
            "timestamp": '1728030156240',
            "signature": "413F4F2F116EC350FFA8164BAA81694269B8A74A",
            "appkey": "298292d4-817f-4d39-b7f6-e658ea9d2fdf",
            "accept": "*/*",
            "origin": "https://fintechappdr.cgws.com",
            "x-requested-with": "com.cgws.wealth",
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://fintechappdr.cgws.com/h5/information-page/html/information.html?id=2995455',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': "sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22191e4c406022a-0e6be360920756-95e6a2d-289440-191e4c406031b%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%7D%2C%22%24device_id%22%3A%22191e4c406022a-0e6be360920756-95e6a2d-289440-191e4c406031b%22%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkyMjM2Y2EwMzljZDAtMDA0NzRkZTM3YzNlMTYwYy05NWU2YTJkLTI4OTQ0MC0xOTIyMzZjYTAzYWUwYyJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%7D"
        }

        for task in tasks:
            payload = {"data": {"key": f"cgws://ljs/app/home/task/{task}"}}
            response = requests.request("POST", url, json=payload, headers=headers)
            print(response.text)

    def run(self):
        self.sign()

        # for i in range(3):
        #     sleep(1)
        #     self.do_daily_task()


if __name__ == '__main__':
    GreatWallTask().run()
