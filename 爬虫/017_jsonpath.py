import json
import jsonpath

# 这里有个jsonpath的教程链接 http://blog.csdn.net/luxideyao/article/details/77802389

obj = json.load(open('017_jsonpath.json','r',encoding='utf-8'))

# 书店所有书的作者
author_list = jsonpath.jsonpath(obj,'$.store.book[*].author')
print(len(author_list))

# 所有的作者
author_list = jsonpath.jsonpath(obj,'$..author')
print(len(author_list))

# store下面的所有的元素
tag_list = jsonpath.jsonpath(obj,'$.store.*')
print(tag_list)

# store里面所有东西的price
price_list = jsonpath.jsonpath(obj,'$.store..price')
print(price_list)

# 第三个书
book = jsonpath.jsonpath(obj,'$..book[2]')
print(book)