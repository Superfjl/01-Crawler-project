# 使用urllib来获取百度首页的源码
import urllib.request

# 下载网页
# url = "http://www.baidu.com"
# urllib.request.urlretrieve(url=url,filename="baidu.html")

# 下载图片
# url = "https://pic2.zhimg.com/v2-e6f46b380bdf4edcd4b39c9dec24e713_r.jpg"
# urllib.request.urlretrieve(url=url,filename="lisa.jpg")

# 下载视频
url = "http://vod.v.jstv.com/2023/10/02/JSTV_JSYS_1696208833271_33Nd0Qo_1439.mp4"
urllib.request.urlretrieve(url=url,filename="01.mp4")


