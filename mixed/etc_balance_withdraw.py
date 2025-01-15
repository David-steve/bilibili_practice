import requests

from Bili.util.utils import curdate, week_day


def check_weekday():
    weekday = week_day(curdate(), start_week=1)

    if weekday != 3:
        return False

    return True


def withdraw():
    """
    etc 金额提现
    :return:
    """
    if not check_weekday():
        return

    url = "https://hsc.lingruiwlkj.com/web/fronted.php"

    querystring = {"_mall_id": "1847", "r": "api/balance/cash"}

    payload = {"price": 5, "type": "alipay", "use_qrcode": 0, "name": "赖锦威", "mobile": "18776666967"}
    headers = {
        "Host": "hsc.lingruiwlkj.com",
        "Content-Length": "84",
        "X-App-Version": "5.10.39",
        "X-Token": "aHR0cHM6Ly93d3cuempoZWppYW5nLmNvbRNWGREfVnBGE1VNH0JeX0lIChMLBloGCzIJAFZKQg0dGkNGRRdLU0RHHxoEHDhHB01XWUVDRUULGwNVGgJCDgMYCQ82EhoIXAYwBAxWTkAO",
        "X-Form-Id-List": "[]",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309080f)XWEB/11253",
        "X-App-Platform": "wxapp",
        "Content-Type": "application/x-www-form-urlencoded",
        "Xweb_xhr": "1",
        "X-Requested-With": "XMLHttpRequest",
        "X-Access-Token": "Z90Ms72AzCSCTYfAuZfaniGHGJ73441K",
        "Accept": "*/*",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://servicewechat.com/wxbe41f480e551a832/5/page-frame.html",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "content-type": "application/x-www-form-urlencoded"
    }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    print(response.text)


if __name__ == '__main__':
    withdraw()
