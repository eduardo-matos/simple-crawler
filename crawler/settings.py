# coding: utf-8

BOT_NAME = 'crawler'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'

ITEM_PIPELINES = {
  'crawler.pipelines.DuplicatesPipeline': 100
}
