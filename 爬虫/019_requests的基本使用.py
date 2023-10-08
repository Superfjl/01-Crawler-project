import requests

url = 'http://www.baidu.com'

response = requests.get(url=url)
# 设置响应的编码格式
response.encoding = 'utf-8'
# 以字符串的形式来返回网页的源码
content = response.text
# 返回一个url地址
url = response.url
# 返回的是二进制的数据
content = response.content
# 返回响应的状态码
status = response.status_code
# 返回响应头
headers = response.headers