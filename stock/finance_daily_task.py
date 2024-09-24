from history_gold_price_service import get_yesterday_gold_price
from mixed.etc_balance_withdraw import withdraw
from mixed.greatwall_daily_tasks import GreatWallTask
from stock_service import get_today_stock_info


if __name__ == '__main__':
    get_yesterday_gold_price()
    get_today_stock_info()
    withdraw()
    GreatWallTask().run()
