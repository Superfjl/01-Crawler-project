import urllib.request

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

# 请求对象的定制
request = urllib.request.Request(url = url,headers= headers)

# 模拟浏览器访问服务器
# response = urllib.request.urlopen(request)

proxies = {
    # 若程序一直无法运行，肯定是这个代理IP不能用啦
    # 去这个网站能免费使用IP https://www.kuaidaili.com/
    'http':'27.76.204.11:4004'
}
# handler  build_opener  open
handler = urllib.request.ProxyHandler(proxies = proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

# 获取响应的信息
content = response.read().decode('utf-8')

# 保存
with open('daili.html','w',encoding='utf-8')as fp:
    fp.write(content)

