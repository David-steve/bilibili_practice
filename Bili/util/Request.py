import requests

from Bili.BilibliInfo import BilibliInfo

Bili = BilibliInfo.get_instance()


class Request:
    headers = {
        "connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
        "referer": "https://www.bilibili.com/",
        "accept": "application/json, text/plain, */*",
        "Content-Type": "application/x-www-form-urlencoded",
        "charset": "UTF-8",
        "Cookie": Bili.get_cookies()
    }
    session = requests.session()

    @classmethod
    def get(cls, url: str):
        try:
            ret = cls.session.get(url=url, headers=cls.headers)
        except Exception as e:
            print(e)
            return None

        return ret

    @classmethod
    def post(cls, url: str, body: str):
        data = body.encode(encoding='utf8')
        ret = cls.session.post(url=url, headers=cls.headers, data=data)
        return ret
