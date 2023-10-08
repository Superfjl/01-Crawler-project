import requests

url = "https://www.baidu.com"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
# get请求，原来得拼接到url中，现在不用啦
data = {
    'wd': '北京'
}

# url  请求资源路径
# params 参数
# kwargs 字典
response = requests.get(url=url,params=data,headers=headers)
response.encoding='utf-8'
text = response.text
print(text)

# 总结：
# （1）参数使用params传递
# （2）参数无需urlencode编码
# （3）不需要请求对象的定制
# （4）请求资源路径中的？可以加也可以不加