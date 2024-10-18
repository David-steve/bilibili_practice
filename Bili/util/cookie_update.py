import orm.manage
import json

from Bili.db.models import Cookies


def cookie_extract(cookie_text: str):
    param = cookie_text.split(";")
    param = dict(map(lambda x: x.strip().split("="), param))

    return json.dumps(param)


if __name__ == '__main__':
    cookie = "buvid3=58039347-0116-9378-A8E4-569BA63E04FD11740infoc; b_nut=1704447011; _uuid=6D5A51078-7848-4998-CA31-EA26F58510EA813167infoc; buvid4=5C27AD7D-6EF0-C163-490A-B68F0D15EB8512915-024010509-EM7YwFs9UXhb6nTbZ7EdVQ%3D%3D; buvid_fp=61f225fc8bf6d6e3d97392c48241a099; rpdid=|(J|~|YRl)Yl0J'u~|RRR~|uJ; DedeUserID=106616461; DedeUserID__ckMd5=d3a0b8dce8d7df66; CURRENT_FNVAL=4048; enable_web_push=ENABLE; iflogin_when_web_push=1; header_theme_version=CLOSE; is-2022-channel=1; home_feed_column=5; CURRENT_QUALITY=80; FEED_LIVE_VERSION=V_HEADER_LIVE_NO_POP; LIVE_BUVID=AUTO9417140530613458; PVID=1; browser_resolution=2048-991; b_lsid=5FB28596_19213188B60; bsource=search_bing; SESSDATA=1900a3d7%2C1742449230%2C9cb9f%2A92CjDI1a5HsBtE9sqrm0pIk1Vp7DG32LQTjJ3a90ewqv-nBjcG43IDM0Xk9dEmtMRHsP0SVmlSclVlaXlURktVX09Gcldva09OQjV3Q2dYSWhGYmRNSy1Zd1lCRTllSFpPR2U4eEpGR1NjVHgzZUcxb280Yng1U25MVldRcWFBbmxlcnE1Q0Q3NElnIIEC; bili_jct=36823b90518017de87bf1394cc07ce21; sid=855ehi69"
    ret = cookie_extract(cookie)

    cookie = Cookies.objects.filter(state=0, website="bilibili").first()
    cookie.cookie_value = ret
    cookie.save()
    print(ret)
