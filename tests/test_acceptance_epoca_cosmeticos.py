# coding: utf-8

from unittest import TestCase
import requests
from scrapy.http import Request, HtmlResponse
from crawler.spiders.spider import EpocaCosmeticosSpider

BASE_URL = 'http://www.epocacosmeticos.com.br'

def scrapy_response(url):
    http_response = requests.get(url)
    request = Request(url=url)
    response = HtmlResponse(url=url, request=request, body=http_response.content)
    return response, http_response.status_code


class SpiderAcceptanceTest(TestCase):
    def test_rules_link_extractor(self):
        link_extractor = EpocaCosmeticosSpider.rules[0].link_extractor
        body, status = scrapy_response(BASE_URL)

        if status == 404: self.fail('Home page not found!')

        links = link_extractor.extract_links(body)
        self.assertTrue(len(links) > 0, 'There are no links to product page')

    def test_parse_yield_correct_item(self):
        links = [
            BASE_URL + '/gabriela-sabatini-eau-de-toilette-gabriela-sabatini-perfume-feminino/p',
            BASE_URL + '/212-nyc-men-body-spray-carolina-herrera-perfume-masculino-para-o-corpo/p',
            BASE_URL + '/laguna-eau-de-toilette-salvador-dali-perfume-feminino/p',
            BASE_URL + '/miss-gabriela-eau-de-toilette-gabriela-sabatini-perfume-feminino/p',
            BASE_URL + '/glow-eau-de-toilette-jennifer-lopez-perfume-feminino/p'
        ]

        spider = EpocaCosmeticosSpider()

        for link in links:
            response, status = scrapy_response(link)

            if status == 404: continue

            item = spider.parser(response).next()
            self.assertEquals(link, item['url'])
            self.assertTrue(len(item['name']) > 0, 'Product has no name')
            self.assertTrue(item['price'] > 0, 'Product has no price')

            return

        self.fail('No products exist')
