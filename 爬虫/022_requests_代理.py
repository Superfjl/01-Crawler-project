import requests

url = 'http://www.baidu.com/s'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
}

data = {
    'wd':'ip'
}

proxy = {
    # 这个代理IP可能会有问题，你可以去快代理中找可用的ip
    'http':'212.129.251.55:16816'
}

response = requests.get(url=url,params=data,headers=headers,proxies=proxy)
response.encoding='utf-8'
context = response.text
print(context)