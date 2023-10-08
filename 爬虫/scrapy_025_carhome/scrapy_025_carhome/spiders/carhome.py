import scrapy


class CarhomeSpider(scrapy.Spider):
    name = 'carhome'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/price/brand-33.html']

    def parse(self, response):
        print("+++++++++++++++++++++++++")
        name_list = response.xpath("//div[@class='main-title']/a/text()")
        for name in name_list:
            print(name.extract())
        price_list = response.xpath("//div[@class='main-lever-right']/div/span/span/text()")
        for price in price_list:
            print(price.extract())
        print("********************")
        pass
