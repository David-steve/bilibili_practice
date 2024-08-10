from typing import Generator, Any, Iterator, List

import requests

import orm.manage
from stock.entity.history_gold_price import HistoryGoldPrice


def get_gold_price():
    url = "https://www.sge.com.cn/graph/Dailyhq"

    payload = "instid=Au99.99"
    headers = {
        "Origin": "https://www.sge.com.cn",
        "Referer": "https://www.sge.com.cn/sjzx/mrhq",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "content-type": "application/x-www-form-urlencoded"
    }

    return requests.request("POST", url, data=payload, headers=headers)


def parse(rows: Iterator[List[Any]]) -> Generator[HistoryGoldPrice, Any, None]:
    for row in rows:
        date = row[0]
        open_price = row[1]
        close_price = row[2]
        high_price = row[3]
        low_price = row[4]

        yield HistoryGoldPrice(date=date, open_price=open_price, close_price=close_price, high_price=high_price,
                               low_price=low_price)


def get_history_price():
    response = get_gold_price()
    json_data = response.json()
    rows = json_data['time']

    print(response.json)
    gold_prices = parse(rows)

    for gold_price in gold_prices:
        if not gold_price:
            continue

        print(gold_price)
    # exit()


def get_yesterday_gold_price():
    """
    获取昨天的金价行情
    :return: None
    """
    response = get_gold_price()
    json_data = response.json()
    rows = json_data['time']

    gold_prices = parse([rows[-1]])
    for gold_price in gold_prices:
        print(gold_price)

        try:
            gold_price.save()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    get_yesterday_gold_price()
