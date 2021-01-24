


import scrapy
from scrapy.selector import Selector

from ..items import HongxiuSpiderItem


class BookSpider(scrapy.Spider):
    name="book"
    allowed_domains=['hongxiu.com']
    # start_url=['https://www.hongxiu.com/all?pageSize=10&gender=2&catId=-1&pageNum=1']
    def start_requests(self):
        for i in range(1,10):
            yield scrapy.Request(url="https://www.hongxiu.com/all?pageSize=10&gender=2&catId=-1&pageNum=%d"%i,
                                callback=self.get_book_url  )

    def get_book_url(self,respone):
        print("输出详情页网址")
        Details_page_url=respone.xpath("//h3//a/@href").extract()
        for i in Details_page_url:
            url="https://www.hongxiu.com"+i
            yield scrapy.Request(url,callback=self.get_detail)
    def get_detail(self,respone):
        type=respone.xpath("//div[@class='book-info']/p[@class='tag-box']//i[not(@class)]/text()").getall()
        # 小说属性
        print(type)



        #  scrapy ----   welcome to me
        #
        # An open source and collaborative framework
        # for extracting the data you need from websites.
        # In a fast, simple, yet extensible way.



        name=respone.xpath("//h1//em/text()").get()
        #小说名字
        print(name)

        author=respone.xpath("//a[@class='writer default']/text()").get().replace(" 著","")
        #小说作者
        print(author)

        numbers_words=respone.xpath("//p[@class='total']/span[1]/text()").get()+respone.xpath("//p[@class='total']/em[1]/text()").get()
        #小说字数
        print(numbers_words)

        Collection=respone.xpath("//p[@class='total']/span[2]/text()").get()+respone.xpath("//p[@class='total']/em[2]/text()").get()
        #收藏数量
        print(Collection)

        introduction=respone.xpath("//p[@class='intro']/text()").getall()
        #小说简介
        print(introduction)

        Photo_Url=respone.xpath("//a[@id='bookImg']/img/@src").get().replace("//","")
        #小说简介图
        print(Photo_Url)



        item=HongxiuSpiderItem()

        item['type']=type
        item['name']=name
        item['author']=author
        item['numbers_words']=numbers_words
        item['Collection']=Collection
        item['introduction']=introduction
        item['Photo_Url']=Photo_Url

        yield item




