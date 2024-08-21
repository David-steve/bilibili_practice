from typing import Generator, Any, Dict

from Bili.db.models import Cookies
from Bili.util.utils import week_day, curdate

import requests
from requests import Response

import orm.manage
from Bili.util.utils import from_unix_time, to_unix_time, curdate, date_add, now
from stock.entity.stock import Stock, StockTrace, FocusStock


def get_stock_info(stock_symbol: str = '', begin_date: str = '2024-08-06', count="7", mode="before"):
    timestamp = int(to_unix_time(begin_date))

    if mode == "before":
        count = int(count) * -1

    url = "https://stock.xueqiu.com/v5/stock/chart/kline.json"

    querystring = {"symbol": stock_symbol, "begin": f"{timestamp * 1000}", "period": "day", "type": mode,
                   "count": count}

    print(querystring)
    # exit()
    cookie:Cookies = Cookies.objects.filter(website='雪球').first()

    headers = {
        "origin": "https://xueqiu.com",
        "referer": "https://xueqiu.com/S/SZ002594",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Cookie": cookie.cookie_value
    }

    return requests.request("GET", url, headers=headers, params=querystring)


def response_parse(response: Response) -> Dict[str, Any]:
    json_data = response.json()
    error_code = json_data['error_code']
    data = json_data['data']

    if error_code != 0 or not data:
        print("error_code:", error_code)
        return {}

    return data


def parse(data: Dict[str, Any]) -> Generator[StockTrace, Any, None]:
    symbol = data['symbol']
    items = data['item']
    column = data['column']

    stock = Stock.objects.filter(code=symbol).first()
    if not stock:
        print("找不到该股票信息: ", symbol)
        return None

    for item in items:
        if len(item) < 10:
            print("item:", item)
            continue

        info = dict(zip(column, item))

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
        print("close_price: ", close_price)

        yield StockTrace(stock=stock, date=date, open_price=open_price, high_price=high_price, low_price=low_price,
                         close_price=close_price, change_price=change_price, change_rate=change_rate, volume=volume,
                         turnover_amt=turnover_amt, turnover_rate=turnover_rate)


def get_stock_history_info(stock_code: str = 'SZ002594', begin_date: str = '2024-08-01', count="7"):
    response = get_stock_info(stock_symbol=stock_code, begin_date=begin_date, count=count)
    data = response_parse(response)

    if not data:
        print("获取数据失败, status_code: ", response.status_code)
        return

    print(response.text)

    stock = Stock.objects.filter(code=stock_code).first()
    if not stock:
        stock = Stock(code=stock_code, name=stock_code).save()

    stocks = parse(data)
    if not stocks:
        # 解析失败
        return

    for stock in stocks:
        if not stock:
            continue

        stock_trace = StockTrace.objects.filter(stock=stock.stock, date=stock.date).first()
        if stock_trace:
            stock.id = stock_trace.id
            stock.create_time = stock_trace.create_time

        try:
            stock.save()
        except Exception as e:
            print(e)


def get_today_stock_info():
    weekday = week_day(curdate(), start_week=1)

    if weekday in (6, 7):
        # 周六日闭市
        return

    focus_stocks = FocusStock.objects.filter(del_flag=False)

    for focus_stock in focus_stocks:
        stock_code = focus_stock.stock.code
        # today = curdate()
        today = now()
        # date = date_add(today, 1, date_format_='%Y-%m-%d %H:%M:%S')

        print(stock_code)
        response = get_stock_info(stock_symbol=stock_code, begin_date=today, count="1")
        print(response.text)

        data = response_parse(response)
        if not data:
            print("获取数据失败, status_code: ", response.status_code)
            return

        print(data)

        stocks = parse(data)
        for stock in stocks:
            print(stock.date, stock.close_price)
            stock_trace = StockTrace.objects.filter(stock=stock.stock, date=stock.date).first()
            if stock_trace:
                stock.id = stock_trace.id
            stock.save()


if __name__ == '__main__':
    get_stock_history_info(stock_code="SZ300750", begin_date="2024-08-07", count="365")
    # get_today_stock_info()
