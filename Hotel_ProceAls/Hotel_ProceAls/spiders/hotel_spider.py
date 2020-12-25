import scrapy


class HotelSpiderSpider(scrapy.Spider):
    name = 'hotel_spider'
    allowed_domains = ['hotel.meituan.com']
    start_urls = ['http://hotel.meituan.com/']

    def parse(self, response):
        pass
