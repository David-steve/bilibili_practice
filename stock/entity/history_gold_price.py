from django.db import models


class HistoryGoldPrice(models.Model):
    date = models.DateField(verbose_name="日期")
    open_price = models.DecimalField(verbose_name="开盘价", max_digits=10, decimal_places=2)
    close_price = models.DecimalField(verbose_name="收盘价", max_digits=10, decimal_places=2)
    high_price = models.DecimalField(verbose_name="最高价", max_digits=10, decimal_places=2)
    low_price = models.DecimalField(verbose_name="最低价", max_digits=10, decimal_places=2)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    class Meta:
        db_table = "history_gold_price"

    def __str__(self):
        return f"date: {self.date}, open_price: {self.open_price}, close_price: {self.close_price}," \
               f" high_price: {self.high_price}, low_price: {self.low_price}"
