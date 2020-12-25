import scrapy



class QuotesSpider(scrapy.Spider):
    name="quotes"
    # def start_requests(self):
    #     urls = [
    #         'http://quotes.toscrape.com/page/1/',
    #         'http://quotes.toscrape.com/page/2/',
    #     ]
    #
    #     for url in  urls:
    #         yield scrapy.Request(url=url,callback=self.parse)

    def start_request(self):
        url='http://quotes.toscrape.com/'
        tag=getattr(self,'tag',None)
        if tag is not None:
            url=url+'tag/'+tag
        yield scrapy.Request(url,self.parse())


    def parse(self,response):
        for quote in response.css("div.quote"):
            yield {
                'text':quote.css("span.text::text").get(),
                'author':quote.css("small.author::text").get(),
                'tags':quote.css("div.tags a.tag::text").getall(),

            }
        next_page=response.css('li.next a::attr(href)').get()


        #选择选择并且爬取下一个
        # if next_page is not None:
        #     next_page=response.urljoin(next_page)
        #     yield scrapy.Request(next_page,callback=self.parse)


        # for href in response.css('ul.pager a::attr(href)'):
        #     #无需调用urljoin 方法，可以直接使用相对路径
        #     yield  response.follow(href,callback=self.parse)


        # #可以自动使用其href属性，因此代码可以进一步缩短
        # for a in response.css('ul.pager a'):
        #     yield  response.follow(a,callback=self.parse)

        # 要从iterable创建多个请求，可以使用response.follow_all() 取而代之
        # anchors=response.css('ul.pager a')
        # yield  from  response.follow_all(anchors,callback=self.parse)

        # 以上缩短，更短

        yield from response.follow_all(css='ul.pager a',callback=self.parse)