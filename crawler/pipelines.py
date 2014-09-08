# coding: utf-8

from scrapy.exceptions import DropItem


class DuplicatesPipeline(object):
    def __init__(self):
        self.product_names = set()

    def process_item(self, item, spider):
        if item['name'] in self.product_names:
            raise DropItem("Duplicate product found: %s" % item)
        else:
            self.product_names.add(item['name'])
            return item
