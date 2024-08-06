from typing import Generator, Any

import requests
from requests import Response

import orm.manage
from Bili.util.utils import from_unix_time, to_unix_time
from stock.entity.stock import Stock, StockTrace


def get_stock_info(stock_symbol: str = '', begin_date: str = '2024-08-06', count="7"):
    timestamp = int(to_unix_time(begin_date))

    url = "https://stock.xueqiu.com/v5/stock/chart/kline.json"

    querystring = {"symbol": stock_symbol, "begin": f"{timestamp * 1000}", "period": "day", "type": "after",
                   "count": count}

    print(querystring)
    # exit()

    headers = {
        "origin": "https://xueqiu.com",
        "referer": "https://xueqiu.com/S/SZ002594",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Cookie": "cookiesu=831720582869863; device_id=670925312d536e47f413d7e647af2023; xq_a_token=fb0f503ef881090db449e976c330f1f2d626c371; xqat=fb0f503ef881090db449e976c330f1f2d626c371; xq_r_token=967c806e113fbcb1e314d5ef2dc20f1dd8e66be3; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTcyNTMyNDc3NSwiY3RtIjoxNzIyODU4NzU5NjAwLCJjaWQiOiJkOWQwbjRBWnVwIn0.E_Ch7OjrIJtkRffEgs86xdumMK0dOtFS6rfTLhdVOrH_z-oSpEHnVnjP72F5EUXAogqxnj5k2dADeK8KPex6gOAcgsmauWGOZfulDYaIuBb4zSKKLwMMWd6FyHJlWc4OolEEHSVWG6P7AHqmkIIoL93447kTl6pFplTeRpcQKbsofPrP9Ijwz_-XGNrdPdLdIR_MbZJACIYEjbkU1DmqMYn_3i-Q52KTlkrdgbAWYBuRCUUgpGPvT9kiIF37ToZz75tkMlP-HoG7B7pZktqiGkC8D0BDPOKBtL-6OiDbR9gPilQSRol45rCW805WwYhAeB19f9AGMqDRFbGniprsXg; u=831720582869863; Hm_lvt_1db88642e346389874251b5a1eded6e3=1720582881,1722858779; HMACCOUNT=5C9D722CF5E66B86; s=cg1203yzea; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1722909422; ssxmod_itna=eqAxR7G=0=qWq7K50dq0PDQFuCjiDgGxbQDGqeery4F5DsNTDSxGKidDqxBnn=hoHK070xK5tzOeb5iqwho7Qv7zrGnLfUK0e0aDbqGkiBQY2eDx6q0rD74irDDxD3Db3QDSDWKD9D0bCy65suxGWDmbCDWPDYxDr26KDRxi7DDH=sx07DQHCd7e17DDz773KemwoApAwsoEz8+5ett0D2xG1C40HtjdK2OoX/+xGtbL65/R8DlKuDCKsSP7788x149yhai0dKj+iIQrbC14o7Dr4LmtHEL04GQ25eYhx=i2Dan2e7DDWqGhloUxYD==; ssxmod_itna2=eqAxR7G=0=qWq7K50dq0PDQFuCjiDgGxbQDGqeery4KikUbooDl=7iDj+hoFzSq5qjpqnNqnQmk2r+t8fkGNYYcOQP6egKQAEE63E8d8H2qGmMomhvycCG2EYdmk3e8SlaGD6XD8oQiY40sBThClMdY0GK5/qvsUdxnDjQmCioDpLrslwt2mDrIeMiVn2QpB3bl9x=4fx=o+4e5b35PHGK3qqo31ciedkA1TL9UlQ54RZBPH+6G2CdQBTdNXStwlT6gSW=9t/WwuWrKacTdOcu=ElmsQtBLKfTIQi0tamNVAlWKrI0bAxh/HVtIbDYh9e4VrViT7Uqh4WDM+bIxrS+q7Wz/xk74RG0R7yfnAxCi6WA7nH1Fa3PK=nuFQhocR=97DHTh3WDH0HCGF0+sDxNZIe=0PkEvCGtYnDIn130BBv=8wsbD/8WcW24TRTlnEiRstc14g8jhFjTbKds4p5uauFH9CAUfKXjrv4uiWA5RPR4T/WR1pBFn3ek4hro8i5RS4ClL3HWDaROTgWeeduoRI4zTaRSHmgCDcBx4BHIRzrwNY0qN1RbGdD07eDqyAC/Bq/A5No9uFfdoxKequCxma3g7KZadcq5t7O12BP8IRUUP5ew4wMAfIGyoGSUTN7GkPsbUuadGghNFrAYqDDLxD20GDD==="
    }

    return requests.request("GET", url, headers=headers, params=querystring)


def parse(response: Response) -> Generator[StockTrace, Any, None]:
    json_data = response.json()
    error_code = json_data['error_code']
    infos = json_data['data']

    if error_code != 0 or not infos:
        print("error_code:", error_code)
        return None

    symbol = infos['symbol']
    items = infos['item']

    stock = Stock.objects.filter(code=symbol).first()
    if not stock:
        stock = Stock(code=symbol, name=symbol).save()

    for item in items:
        if len(item) < 10:
            print("item:", item)
            continue

        timestamp = item[0]
        # 成交量
        volume = item[1]
        # 开盘价
        open_price = item[2]
        # 最高价
        high_price = item[3]
        # 最低价
        low_price = item[4]
        # 收盘价
        close_price = item[5]
        # 涨跌额
        change_price = item[6]
        # 涨跌幅
        change_rate = item[7]
        # 换手率
        turnover_rate = item[8]
        # 成交额
        turnover_amt = item[9]
        date = from_unix_time(timestamp / 1000)

        yield StockTrace(stock=stock, date=date, open_price=open_price, high_price=high_price, low_price=low_price,
                         close_price=close_price, change_price=change_price, change_rate=change_rate, volume=volume,
                         turnover_amt=turnover_amt, turnover_rate=turnover_rate)


def get_stock_history_info(stock_code: str = 'SZ002594', begin_date: str = '2024-08-01', count="7"):
    stock = Stock.objects.filter(code=stock_code).first()
    if not stock:
        stock = Stock(code=stock_code, name=stock_code).save()

    response = get_stock_info(stock_symbol=stock_code, begin_date=begin_date, count=count)
    print(response.text)

    stocks = parse(response)
    if not stocks:
        # 解析失败
        return

    for stock in stocks:
        if not stock:
            continue

        # print(stock.date, stock.open_price, stock.high_price, stock.low_price, stock.close_price,
        #       stock.change_price, stock.change_rate, stock.volume, stock.turnover_amt, stock.turnover_rate)
        # exit()
        stock.save()


if __name__ == '__main__':
    get_stock_history_info(stock_code="01810", begin_date="2024-01-31", count="365")
