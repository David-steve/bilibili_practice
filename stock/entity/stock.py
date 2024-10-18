from django.db import models


class Stock(models.Model):
    code = models.CharField(verbose_name="股票代码", max_length=10)
    name = models.CharField(verbose_name="股票名称", max_length=20)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    class Meta:
        db_table = "stock"


class StockTrace(models.Model):
    date = models.DateField(verbose_name="日期")
    stock = models.ForeignKey(Stock, verbose_name="股票", on_delete=models.DO_NOTHING)
    open_price = models.DecimalField(verbose_name="开盘价", max_digits=10, decimal_places=3)
    close_price = models.DecimalField(verbose_name="收盘价", max_digits=10, decimal_places=3)
    high_price = models.DecimalField(verbose_name="最高价", max_digits=10, decimal_places=3)
    low_price = models.DecimalField(verbose_name="最低价", max_digits=10, decimal_places=3)
    change_rate = models.DecimalField(verbose_name="涨跌幅", max_digits=10, decimal_places=2)
    change_price = models.DecimalField(verbose_name="涨跌额", max_digits=10, decimal_places=2)
    volume = models.BigIntegerField(verbose_name="成交量")
    turnover_amt = models.DecimalField(verbose_name="成交额", max_digits=10, decimal_places=2)
    turnover_rate = models.DecimalField(verbose_name="换手率", max_digits=10, decimal_places=2)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now=True)

    class Meta:
        db_table = "stock_trace"


class FocusStock(models.Model):
    stock = models.ForeignKey(Stock, verbose_name="股票", on_delete=models.DO_NOTHING)
    up_rate_remind = models.DecimalField(verbose_name="涨幅提醒", max_digits=10, decimal_places=2)
    down_rate_remind = models.DecimalField(verbose_name="跌幅提醒", max_digits=10, decimal_places=2)
    price_remind = models.DecimalField(verbose_name="到达指定股价提醒", max_digits=10, decimal_places=2)
    # yesterday_kline_10 = models.DecimalField(verbose_name="昨日10日K线图", max_digits=10, decimal_places=2)
    # yesterday_kline_30 = models.DecimalField(verbose_name="昨日30日K线图", max_digits=10, decimal_places=2)
    # yesterday_kline_50 = models.DecimalField(verbose_name="昨日50日K线图", max_digits=10, decimal_places=2)
    del_flag = models.BooleanField(verbose_name="删除标记", default=False)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)

    class Meta:
        db_table = "focus_stock"


class GridTrade(models.Model):
    # 编号
    id = models.AutoField(primary_key=True)
    symbol = models.CharField(max_length="32", verbose_name="代码")
    name = models.CharField(max_length="64", verbose_name="名字")
    base_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="基准价")
    price_range_top = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="价格区间顶部")
    price_range_bottom = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="价格区间底部")

    rise_ratio = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="上升比例")
    fall_ratio = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="下跌比例")
    trade_shares = models.IntegerField(verbose_name="每次交易股数")
    buy_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="买入价格")
    sell_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="卖出价格")
    current_shares = models.IntegerField(verbose_name="当前持有数量")
    # 最大持仓金额, 超出不再买入
    max_holding_amount = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="最大持仓金额")
    # 最小持仓金额, 低于此金额不再卖出
    min_holding_amount = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="最小持仓金额")

    last_price = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True, verbose_name="上一次价格")
    # 期待买入价格: 上一次卖出或买入价格 * (1- 网格比例)
    exp_buy_price = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    # 期待买入价格: 上一次卖出或买入价格 * (1 + 网格比例)
    exp_sell_price = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    del_flag = models.SmallIntegerField(verbose_name="删除标记")
    state = models.SmallIntegerField(verbose_name="状态 0暂停 1正常")

    class Meta:
        db_table = "grid_trade"
        verbose_name = "网格交易"

    def __str__(self):
        return f"GridTrade {self.id}: Base Price {self.base_price}, Price Range {self.price_range_top}," \
               f" Rise/Fall Ratio {self.rise_ratio} {self.fall_ratio}"


class TradeRecord(models.Model):
    # 关联网格交易
    grid_trade = models.ForeignKey(GridTrade, on_delete=models.DO_NOTHING)
    trade_time = models.DateTimeField(auto_now_add=True, verbose_name="交易时间")
    trade_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="交易价格")
    trade_type = models.CharField(max_length=10, choices=(('buy', '买入'), ('sell', '卖出')), verbose_name="交易类型")
    trade_shares = models.IntegerField(verbose_name="交易股数")
    current_shares = models.IntegerField(verbose_name="当前持有数量")
    # 该笔交易持有数量
    keep_shares = models.IntegerField(verbose_name="该笔交易持有数量")

    def __str__(self):
        return f"TradeRecord : {self.trade_type} at {self.trade_price} on {self.trade_time}"

    class Meta:
        db_table = "trade_record"
        verbose_name = "交易记录"
