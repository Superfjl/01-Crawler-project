# 使用urllib来获取百度首页的源码
import urllib.request
# (1)定义一个url  就是你要访问的地址
URL = "http://www.baidu.com"

# (2)模拟浏览器向服务器发送请求 response响应
response = urllib.request.urlopen(URL)

# （3）获取响应中的页面的源码  content 内容的意思
# read方法  返回的是字节形式的二进制数据
# 我们要将二进制的数据转换为字符串
# 二进制--》字符串  解码  decode('编码的格式')

content = response.read().decode("utf-8")

print(content)

