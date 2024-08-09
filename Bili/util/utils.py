import time
from datetime import datetime
from dateutil.relativedelta import relativedelta


def from_unix_time(from_time) -> str:
    """
    将给定的 Unix时间戳转换为时间字符串
    :param from_time:
    :return:
    """
    import datetime as dt
    return dt.datetime.fromtimestamp(from_time).strftime("%Y-%m-%d")


def to_unix_time(from_time, time_format="%Y-%m-%d") -> float:
    """
    将给定的时间字符串转换为 Unix时间戳
    :param from_time:
    :param time_format:
    :return:
    """
    import datetime as dt
    if ':' in from_time:
        time_format = "%Y-%m-%d %H:%M:%S"

    return dt.datetime.strptime(from_time, time_format).timestamp()


def get_current_date() -> str:
    return time.strftime("%Y-%m-%d", time.localtime())


curdate = get_current_date


def date_format(date, input_format="%Y-%m-%d", output_format="%Y-%m-%d"):
    date_obj = datetime.strptime(date, input_format)
    return date_obj.strftime(output_format)


def date_add(date: str, num, interval: str = 'days', date_format_='%Y-%m-%d') -> str:
    t = datetime.strptime(date, date_format_)
    if interval in ('days', 'weeks', 'months', 'years', 'day', 'month', 'years', 'microseconds'):
        param = {interval: num}
        date = t + relativedelta(**param)

    if date_format_ != '%Y-%m-%d %H:%M:%S':
        return date_format(str(date), input_format='%Y-%m-%d %H:%M:%S', output_format=date_format_)

    return str(date)


def now() -> str:
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
