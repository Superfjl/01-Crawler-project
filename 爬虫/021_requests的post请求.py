import requests

url = "https://fanyi.baidu.com/sug"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

data = {
    'kw': 'eye'
}

# url 请求地址
# data 请求参数
# kwargs 字典
response = requests.post(url=url,data=data,headers=headers)
response.encoding='utf-8'
content = response.text
print(type(content))
# 把JSON格式的数据转化为Python对象
import json
obj = json.loads(content)
print(type(obj))

