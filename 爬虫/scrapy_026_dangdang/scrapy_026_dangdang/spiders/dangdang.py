import scrapy
from scrapy_026_dangdang.items import Scrapy026DangdangItem

class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['bang.dangdang.com']
    start_urls = ['http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent7-0-0-1-1']
    """
    第一页 
http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent7-0-0-1-1
    第二页
http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent7-0-0-1-2
    第三页
http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent7-0-0-1-3
    """
    base_url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent7-0-0-1-'
    page = 1
    def parse(self, response):
        print("+++++++++++++++++++++++++++++++++++++")
        li_list = response.xpath('//ul[@class="bang_list clearfix bang_list_mode"]/li')
        for li in li_list:
            src = li.xpath('.//div[@class="pic"]//img/@src').extract_first()

            name = li.xpath('.//div[@class="name"]/a/@title').extract_first()

            price = li.xpath('.//div[@class="price"]/p/span[1]/text()').extract_first()

            book = Scrapy026DangdangItem(src=src,name=name,price=price)
            # 获取一个book就将book交给pipelines
            yield book
        if self.page < 10:
            self.page = self.page + 1
        url = self.base_url + str(self.page)
        #             怎么去调用parse方法
        #             scrapy.Request就是scrpay的get请求
        #             url就是请求地址
        #             callback是你要执行的那个函数  注意不需要加（）
        yield scrapy.Request(url=url,callback=self.parse)
        print("-------------------------------------")

        pass
