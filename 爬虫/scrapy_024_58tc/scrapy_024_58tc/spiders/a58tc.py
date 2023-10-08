import scrapy


class A58tcSpider(scrapy.Spider):
    # 运行爬虫文件时使用的名字
    name = '58tc'
    # 爬虫允许的域名，在爬取的时候，如果不是此域名之下的url会被过滤掉
    allowed_domains = ['bj.58.com']
    # 声明爬虫的起始地址，URL后若有斜杠的话直接去掉
    start_urls = ['http://bj.58.com']
    # 解析数据的回调函数
    def parse(self, response):
        print("************************")
        # 响应的是字符串
        print(response.text)
        # 响应的是二进制文件
        print(response.body)
        # xpath()方法的返回值类型是selector类型的列表
        print(type(response.xpath('')))
        # extract()方法提取的是selector对象的data
        print(response.extract())
        # extract_first()方法提取的是selector列表中的第一个数据
        pass
