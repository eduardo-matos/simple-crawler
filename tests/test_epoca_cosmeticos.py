# coding: utf-8

from unittest import TestCase
from decimal import Decimal
from path import path
from scrapy.http import Request, HtmlResponse
from crawler.spiders.spider import EpocaCosmeticosSpider

BASE_URL = 'http://example.com'

def load_file(file_path):
    return path('tests/' + file_path).bytes()

def scrapy_response(file_path):
    request = Request(url=BASE_URL)
    response = HtmlResponse(url=BASE_URL, request=request, body=load_file(file_path))
    return response


class SpiderTest(TestCase):
    def test_base_config(self):
        spider = EpocaCosmeticosSpider()
        self.assertEquals('epoca_cosmeticos', spider.name)
        self.assertEquals(1, len(spider.allowed_domains))
        self.assertEquals('www.epocacosmeticos.com.br', spider.allowed_domains[0])
        self.assertEquals(1, len(spider.start_urls))
        self.assertEquals('http://www.epocacosmeticos.com.br/', spider.start_urls[0])

    def test_has_rules(self):
        spider = EpocaCosmeticosSpider()
        self.assertEquals(1, len(spider.rules))

    def test_rules_link_extractor(self):
        spider = EpocaCosmeticosSpider()
        link_extractor = spider.rules[0].link_extractor
        links = link_extractor.extract_links(scrapy_response('dummy_page_with_links.html'))
        self.assertEquals(2, len(links))
        self.assertEquals(BASE_URL + '/ham/p', links[0].url)
        self.assertEquals(BASE_URL + '/spam/p', links[1].url)

    def test_parse_yield_correct_item(self):
        response = scrapy_response('dummy_product_page.html')

        spider = EpocaCosmeticosSpider()

        item = spider.parser(response).next()
        self.assertEquals(BASE_URL, item['url'])
        self.assertEquals('Random product name', item['name'])
        self.assertEquals(Decimal('79.02'), item['price'])
