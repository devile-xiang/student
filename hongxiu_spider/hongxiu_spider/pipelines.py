# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import JsonItemExporter, JsonLinesItemExporter


class HongxiuSpiderPipeline(object):
    # def __init__(self):
    #     self.fp=open("hongxiu.json",'wb')
    #     self.exporter=JsonItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')
    #     self.exporter.start_exporting()
    #
    #
    # def process_item(self, item, spider):
    #     self.exporter.export_item(item)
    #     return item
    # def close_spider(self,spider):
    #     self.exporter.finish_exporting()
    #     self.fp.close()
    #         def __init__(self):
    #             self.fp = open("duanzi.json", "wb")
    #             self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')
    #         def open_spider(self, spider):
    #             pass
    #
    #         def process_item(self, item, spider):
    #             self.exporter.export_item(item)
    #             return item
    #         def close_spider(self, spider):
    #             self.fp.close()
    def __init__(self):
        self.fp = open("story.json", "wb")  # 管道类初始化，以wb二进制打开文件，二进制没有编码形式
        # ensure_ascii=False:以中文字符保存
        self.exporter = JsonItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')
        self.exporter.start_exporting()  # 以标识 exporting 过程的开始。

    def open_spider(selfs, spider):  # 爬虫开始前，执行
        print('开始了')

    def process_item(self, item, spider):  # 爬虫开始过程，执行
        self.exporter.export_item(item)  # 爬虫获取到的每项item数据的处理方法
        return item

    def close_spider(self, spider):  # 爬虫结束后，执行
        self.exporter.finish_exporting()  # 以标识 exporting 过程的结束。
        self.fp.close()
        print("over")