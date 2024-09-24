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
            "Timestamp": "1726650167163",
            "Signature": "3a26a6379b749969bea611033b19216c6a798472",
            "Nonce": "562215",
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
    def read_news():
        url = "https://fintechappdr.cgws.com/api/business-credit-mall/app/report/send"

        payload = {"data": {"key": "cgws://ljs/app/home/task/dailyReadingInformation"}}
        headers = {
            "Host": "fintechappdr.cgws.com",
            "Content-Length": "67",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Nonce": "003315",
            "User-Agent": "Mozilla/5.0 (Linux; Android 12; PEEM00 Build/RKQ1.211103.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046285 Mobile Safari/537.36CustomUserAgent_C_4.15.0_Android elderMode_0",
            "Content-Type": "application/json; charset=UTF-8",
            "Sessionid": "eb2cab58-f6e4-43ef-b8f4-c5b5c4c50ce6",
            "Timestamp": "1726650283673",
            "Signature": "FCBCBBE160646F1C3B8A7310EB0CCD4551999C31",
            "Accept": "*/*",
            "Origin": "https://fintechappdr.cgws.com",
            "X-Requested-With": "com.cgws.wealth",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://fintechappdr.cgws.com/h5/information-page/html/information.html?id=2933014",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            # "Cookie": 'ensorsdata2015jssdkcross={"distinct_id":"191e4c406022a-0e6be360920756-95e6a2d-289440-191e4c406031b","first_id":"","props":{"$latest_traffic_source_type":"直接流量","$latest_search_keyword":"未取到值_直接打开","$latest_referrer":"","$latest_referrer_host":""},"$device_id":"191e4c406022a-0e6be360920756-95e6a2d-289440-191e4c406031b"}',
            "content-type": "application/json"
        }

        response = requests.request("POST", url, json=payload, headers=headers)

        print(response.text)

    def run(self):
        self.sign()

        for i in range(3):
            sleep(1)
            self.read_news()


if __name__ == '__main__':
    GreatWallTask().run()
