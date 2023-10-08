# 适用的场景：数据采集的时候 需要绕过登陆 然后进入到某个页面
# 个人信息页面是utf-8  但是还报错了编码错误  因为并没有进入到个人信息页面 而是跳转到了登陆页面
# 那么登陆页面不是utf-8  所以报错

# 什么情况下访问不成功？
# 因为请求头的信息不够  所以访问不成功
import urllib.request
import urllib.parse

"""
分析：
    https://weibo.com/u/5999922935
    get请求 
"""

url = "https://weibo.com/u/5999922935"

# 注意：请求头中有以':'开始的都不是必要的信息，可以直接删掉.还有就是Accept-Encoding这个也是会对爬取数据有影响的
headers = {
        "Host": "weibo.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Connection": "keep-alive",
        "Cookie": "XSRF-TOKEN=hEkPAtA-QZxG_bBFfe5tHz7G; SUB=_2A25IGI_dDeRhGeNH4lsY8izFyDmIHXVrb-YVrDV8PUNbmtAGLWb4kW9NSkd6qyb_qtIj0hut3-CvvZ-rwxkgktKE; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5RLnUHHZYnqWKIzpBV8Ejx5JpX5KzhUgL.Fo-41K.4eoz4e0-2dJLoIpf2gCH8SCHWSFHWSEH81C-4SFHWSFH8SC-4eEHWSBtt; WBPSESS=T0ciApD-FtPQbm-m3y258tMs40dKmpohsfAqHuGEYHaEx5_5w0RBZ0gJle0ssX8Y3VHcRkpQKI9SYDaJfF6Q3BKqnflmHJyFonmKFKpMzT-nh_bWI5DEI37EB5bN-zwIl4KBsSYZSzcrJKNVFUd5EA==; PC_TOKEN=b2b25bcf5a; login_sid_t=3aac9a6ca9f626c4ad133b9f789f5b1d; cross_origin_proto=SSL; WBStorage=4d96c54e|undefined; _s_tentry=weibo.com; Apache=7660251434007.883.1696399189820; SINAGLOBAL=7660251434007.883.1696399189820; ULV=1696399189820:1:1:1:7660251434007.883.1696399189820:; wb_view_log=1920*10801; ALF=1727935245; SSOLoginState=1696399246",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

with open("weibo.html",'w',encoding='utf-8') as f:
    f.write(content)
