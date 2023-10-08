"""
请求网址:https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx
post请求
那么其请求参数不用拼接在URL中
"""
import requests
from lxml import etree
url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}
# 获取页面的源码
response = requests.get(url = url,headers = headers)
content = response.text

tree = etree.HTML(content)
VIEWSTATE = tree.xpath("//input[@id='__VIEWSTATE']/@value")[0]
VIEWSTATEGENERATOR = tree.xpath("//input[@id='__VIEWSTATEGENERATOR']/@value")[0]
img_url = tree.xpath("//img[@id='imgCode']/@src")[0]
img_url = 'https://so.gushiwen.cn'+img_url

# 有坑
# import urllib.request
# urllib.request.urlretrieve(url=code_url,filename='code.jpg')
# requests里面有一个方法 session（）  通过session的返回值 就能使用请求变成一个对象

session = requests.session()
response_code = session.get(img_url)
# 注意此时要使用二进制数据  因为我们要使用的是图片的下载
content_code = response_code.content
# wb的模式就是将二进制数据写入到文件
with open('code.jpg','wb')as fp:
    fp.write(content_code)

# 获取了验证码的图片之后 下载到本地 然后观察验证码  观察之后 然后在控制台输入这个验证码 就可以将这个值给
# code的参数 就可以登陆

capture = input("请输入验证码:")

# 点击登录，发送请求
url_post = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'

data_post = {
    '__VIEWSTATE': VIEWSTATE,
    '__VIEWSTATEGENERATOR': VIEWSTATEGENERATOR,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '595165358@qq.com',
    'pwd': 'action',
    'code': capture,
    'denglu': '登录',
}

response = session.post(url=url_post,headers=headers,data=data_post)

content = response.text

with open('gushiwen.html','w',encoding= ' utf-8')as fp:
    fp.write(content)

# 想填好下面的data,必须先把这些数据准备好
data = {
    "__VIEWSTATE": VIEWSTATE,
    "__VIEWSTATEGENERATOR": VIEWSTATEGENERATOR,
    "from": "http://so.gushiwen.cn/user/collect.aspx",
    "email": "用户自己的邮箱",
    "pwd": "用户自己的密码",
    "code": "051h",
    "denglu": "登录"
}