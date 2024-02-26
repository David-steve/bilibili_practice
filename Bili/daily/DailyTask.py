import random
from time import sleep

from pymongo import MongoClient

from Bili.Task import Task
from Bili.db.models import ActionRecord, ExpRecord
from Bili.util.Request import Request
from Bili.BilibliInfo import BilibliInfo

Bili = BilibliInfo.get_instance()

uri = 'mongodb+srv://david:1877648mongodb@cluster0.nuinxks.mongodb.net/?ssl=true&retryWrites=true&w=majority'
client = MongoClient(uri)
db = client["internet"]


class DailyTask(Task):
    def run(self):

        try:
            collection = db["bili_video_type"]
            ret = collection.find_one({'分区名称': '时尚区'})
            tid = ret['tid']
        except Exception as e:
            print(e)
            tid = 155

        try:

            random.sample([i for i in range(10)], 5)
            regions = self.get_region(10, tid)
            # regions = self.get_top_recommend(10, 5)

            videos = random.sample(regions, 5)
            self.watch_videos(videos)
            # self.like_batch(videos)

            title = videos[-1].get('title')
            aid = videos[-1].get("aid")
            bvid = videos[-1].get("bvid")

            ret = self.share(aid)
            print(f"分享视频 {title}", "成功" if ret.json().get("code") == 0 else "失败")
            ActionRecord.objects.create(video_name=title, aid=aid, bvid=bvid, way=0, action=ActionRecord.SHARE)

        except Exception as e:
            print(e)

    def watch_videos(self, videos: iter):
        """
        观看多个视频
        :param videos: 视频
        :return:
        """
        for video in videos:
            # 观看进度
            title = video.get('title')
            aid = video.get("aid")
            bvid = video.get("bvid")
            cid = video.get("cid")

            progress = random.randrange(start=1, stop=400)
            ret = self.watch_video(aid, cid, progress)
            print(f"模拟观看视频 {title}", "成功" if ret.json().get("code") == 0 else "失败")

            ActionRecord.objects.create(video_name=title, aid=aid, bvid=bvid, way=0, action=ActionRecord.WATCH)
            sleep(random.randint(2, 10))

    def watch_video(self, aid, cid, progres):
        """
        模拟观看视频
        :param cid: 视频cid号
        :param aid: 视频aid 号
        :param progres: 模拟观看的时间
        :return:
        """
        url = "http://api.bilibili.com/x/v2/history/report"
        body = f"aid={aid}&cid={cid}&progres={progres}&csrf={Bili.bili_jct}".replace("'", '')

        return Request.post(url, body=body)

    def get_video_info(self, aid=None, bvid=None):
        url = 'https://api.bilibili.com/x/web-interface/view'
        if aid:
            param = f"?aid={aid}"
        elif bvid:
            param = f"?bvid={bvid}"
        else:
            return None

        response = Request.get(url + param)
        json_object = response.json()
        if json_object.get("code") != self.SUCCESS:
            return None
        return json_object.get("data")

    def get_top_recommend(self, ps: int = 8, fresh_type: int = 3):
        """
        获取首页推荐视频
        :param fresh_type: 内容相关性，值越大，推荐内容越相关
        :param ps: page_size 每页多少数量
        :return:
        """
        url = 'https://api.bilibili.com/x/web-interface/index/top/rcmd'
        params = f"?fresh_type={fresh_type}&ps={ps}&version=1"
        response = Request.get(url + params)
        if response.status_code != 200:
            print('视频获取失败')
            return []

        json_object = response.json()
        array = json_object.get("data").get("item")

        videos = list()
        for i in array:
            bvid = i.get("bvid")
            aid = self.get_video_info(bvid=bvid).get("aid")
            video = {
                "title": i.get("title"),
                "aid": aid,
                "bvid": bvid,
                "cid": i.get("cid"),
                "is_followed": i.get("is_followed"),
            }

            videos.append(video)

        return videos

    def get_region(self, ps: int, rid):
        """
        获取b站推荐视频
        :param ps: 视频个数
        :param rid: B站分区类型
        :return: list
        """
        params = f"?ps={ps}&rid={rid}"
        url = "https://api.bilibili.com/x/web-interface/dynamic/region"
        response = Request.get(url + params)

        if response.status_code != 200:
            print('视频获取失败')
            return []
        json_object = response.json()
        array = json_object.get("data").get("archives")

        regions = list()
        for i in array:
            region = {
                "title": i.get("title"),
                "aid": i.get("aid"),
                "bvid": i.get("bvid"),
                "cid": i.get("cid"),
            }

            regions.append(region)

        return regions

    def like_batch(self, videos: iter, like=1):
        """
        批量点赞视频
        :param videos: 视频
        :param like: 1 点赞, 2 取消点赞
        :return: None
        """
        for video in videos:
            title = video.get('title')
            aid = video.get("aid")
            bvid = video.get("bvid")

            ret = self.like(aid, like)
            print(f"模拟点赞视频 {video.get('title')}", "成功" if ret.json().get("code") == 0 else "失败")

            ActionRecord.objects.create(video_name=title, aid=aid, bvid=bvid, way=0, action=ActionRecord.LIKE)

            sleep(random.randint(2, 10))

    def like(self, aid, like: int):
        """
        点赞视频
        :param aid: 视频aid号
        :param like: 1 点赞 2 取消点赞
        :return:
        """
        url = 'https://api.bilibili.com/x/web-interface/archive/like'
        body = f"aid={aid}&like={like}&csrf={Bili.bili_jct}&SESSDATA={Bili.sessdata}"

        return Request.post(url, body=body)

    def comic_sign(self):
        """
        漫画签到
        :return: json
        """
        url = 'https://manga.bilibili.com/twirp/activity.v1.Activity/ClockIn'
        body = 'platform=android'

        return Request.post(url, body=body)

    def share(self, aid):
        url = "https://api.bilibili.com/x/web-interface/share/add"
        # body = f"aid={aid}&eab_x=2&ramval=0&source=web_normal&ga=1&csrf={Bili.bili_jct}".replace("'", '')
        body = f"aid={aid}&eab_x=2&ramval=1&source=web_normal&ga=1&csrf={Bili.bili_jct}".replace("'", '')

        return Request.post(url, body=body)
