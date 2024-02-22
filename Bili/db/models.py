from django.db import models


class ActionRecord(models.Model):
    WATCH = 0
    LIKE = 1
    DISLIKE = 2
    SHARE = 3

    ACTION_CHOICES = [
        (WATCH, 'watch'),
        (LIKE, 'like'),
        (DISLIKE, 'dislike'),
        (SHARE, 'share'),
    ]

    video_name = models.CharField(max_length=128, verbose_name="视频名称")
    aid = models.BigIntegerField(verbose_name="视频aid")
    bvid = models.CharField(max_length=64, verbose_name="视频bvid")
    way = models.SmallIntegerField(verbose_name="视频获取方式 0指定视频类型 1首页推荐", choices=ACTION_CHOICES)
    action = models.SmallIntegerField(verbose_name="操作 0,观看 1,点赞 2,取消点赞 3,分享", choices=ACTION_CHOICES)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)
    del_flag = models.SmallIntegerField(verbose_name="删除标记", default=0)

    class Meta:
        db_table = "bili_action_record"
        verbose_name = "bili 事件记录"
        verbose_name_plural = verbose_name


class ExpRecord(models.Model):
    uname = models.CharField(max_length=128, verbose_name="用户名称")
    uid = models.BigIntegerField(verbose_name="用户UID")
    current_exp = models.IntegerField(verbose_name="当前经验值")
    coins = models.DecimalField(verbose_name="硬币数", max_digits=15, decimal_places=2)
    record_date = models.DateField(verbose_name="记录日期", unique=True, auto_now_add=True)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)
    del_flag = models.SmallIntegerField(verbose_name="删除标记", default=0)

    class Meta:
        db_table = "bili_exp_record"
        verbose_name = "经验值记录"
        verbose_name_plural = verbose_name


class Cookies(models.Model):
    user_name = models.CharField(max_length=128, verbose_name="用户名称")
    user_id = models.CharField(max_length=128, verbose_name="用户UID")
    website = models.CharField(max_length=128,verbose_name="站点名称")
    cookie_value = models.TextField(verbose_name="cookie value")
    state = models.SmallIntegerField(verbose_name="状态 0正常, -1过期")
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)
    del_flag = models.SmallIntegerField(verbose_name="删除标记", default=0)

    class Meta:
        db_table = "t_cookies"
        verbose_name = "cookies"
        verbose_name_plural = verbose_name
