# coding: utf-8

import scrapy


class ProductItem(scrapy.Item):
    url=scrapy.Field()
    name=scrapy.Field()
    title=scrapy.Field()
