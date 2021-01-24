# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HongxiuSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    type=scrapy.Field()#小说类型
    name=scrapy.Field()#小说名称
    author=scrapy.Field()#作者
    numbers_words=scrapy.Field()#总字数
    Collection=scrapy.Field()#收藏量
    introduction=scrapy.Field()#简介
    Photo_Url=scrapy.Field() #小说封面
    pass
