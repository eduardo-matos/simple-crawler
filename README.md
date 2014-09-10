# Simple Crawler
[![Build Status](https://travis-ci.org/eduardo-matos/simple-crawler.svg?branch=master)](https://travis-ci.org/eduardo-matos/simple-crawler)

Simple crawler app that searches for product prices, names and urls for each product at epocacosmeticos.com.br

## Installation
run `pip install -r requirements.txt`.

## Exporting as CSV
run `scrapy crawl crawler -o products.csv -t csv`.

## Testing
run `python runtests.py`.

If you want to run only the unit tests, run `python runtests.py SpiderTest`.
