
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem





class PricePipline():
    vtr_Factor=1.15
    def process_item(self,item,spider):
        adapter=ItemAdapter(item)
        if adapter.get('price'):
            if adapter.get('price_excludes_vat'):
                adapter['price']=adapter['price'] * self.vtr_Factor
            return item
        else:
            raise DropItem(f'Missing price in {item}')


if __name__ == '__main__':
    PricePipline.process_item()