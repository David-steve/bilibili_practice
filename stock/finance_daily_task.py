from env_init import init
from history_gold_price_service import get_yesterday_gold_price
from stock_service import get_today_stock_info

init()

if __name__ == '__main__':
    get_yesterday_gold_price()
    get_today_stock_info()
