# 使用urllib来获取百度首页的源码
import urllib.request

url = 'https://www.baidu.com'

# url的组成
# https://www.baidu.com/s?wd=周杰伦

# http/https    www.baidu.com   80/443     s      wd = 周杰伦     #
#    协议             主机        端口号     路径     参数           锚点
# http   80
# https  443
# mysql  3306
# oracle 1521
# redis  6379
# mongodb 27017

# 这个User-agent可以在浏览器中找到
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

# 因为urlopen方法中不能存储字典 所以headers不能传递进去
# 请求对象的定制
request = urllib.request.Request(url=url,headers=headers)

# Open the URL url, which can be either a string or a Request object.
# url这个参数可以是字符串，也可以是request对象
response = urllib.request.urlopen(url=request)

content = response.read().decode("utf-8")

print(content)
