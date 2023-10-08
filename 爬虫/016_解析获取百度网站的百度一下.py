# 获取网页的源码
# 解析的服务器响应的文件  etree.HTML
# 打印

import urllib.request
from lxml import etree
url = "https://www.baidu.com"

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"
}

# 请求对象的定制
request = urllib.request.Request(url=url,headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取网页源码
content = response.read().decode('utf-8')

# 解析网页源码，来获取我们想要的数据
tree = etree.HTML(content)

# 获取想要的数据 xpath返回的是一个列表类型的数据
res = tree.xpath("//input[@id='su']/@value")
print(res)

