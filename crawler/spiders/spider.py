# coding: utf-8

import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ..items import ProductItem


class EpocaCosmeticosSpider(CrawlSpider):
    name = 'epoca_cosmeticos'
    allowed_domains = ['www.epocacosmeticos.com.br']
    start_urls = ['http://www.epocacosmeticos.com.br/']

    rules = (
        Rule(LinkExtractor(allow=(r'/p$',)), callback='parser', follow=True),
    )

    def parser(self, response):
        if response.css('body.produto'):
            url = response.url
            name = response.xpath("//div[contains(@class, 'productName')]/text()").extract()[0]
            price = response.xpath("//title/text()").extract()[0]

            item = ProductItem()
            item['url'] = url
            item['name'] = name
            item['title'] = price

            yield item
