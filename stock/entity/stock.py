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
    open_price = models.DecimalField(verbose_name="开盘价", max_digits=10, decimal_places=2)
    close_price = models.DecimalField(verbose_name="收盘价", max_digits=10, decimal_places=2)
    high_price = models.DecimalField(verbose_name="最高价", max_digits=10, decimal_places=2)
    low_price = models.DecimalField(verbose_name="最低价", max_digits=10, decimal_places=2)
    change_rate = models.DecimalField(verbose_name="涨跌幅", max_digits=10, decimal_places=2)
    change_price = models.DecimalField(verbose_name="涨跌额", max_digits=10, decimal_places=2)
    volume = models.IntegerField(verbose_name="成交量")
    turnover_amt = models.DecimalField(verbose_name="成交额", max_digits=10, decimal_places=2)
    turnover_rate = models.DecimalField(verbose_name="换手率", max_digits=10, decimal_places=2)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    class Meta:
        db_table = "stock_trace"


class FocusStock(models.Model):
    stock = models.ForeignKey(Stock, verbose_name="股票", on_delete=models.DO_NOTHING)
    up_rate_remind = models.DecimalField(verbose_name="涨幅提醒", max_digits=10, decimal_places=2)
    down_rate_remind = models.DecimalField(verbose_name="跌幅提醒", max_digits=10, decimal_places=2)
    price_remind = models.DecimalField(verbose_name="到达指定股价提醒", max_digits=10, decimal_places=2)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    class Meta:
        db_table = "focus_stock"
