# -*- coding: utf-8 -*-
import scrapy,re,jieba,wordcloud



class StocksSpider(scrapy.Spider):
    name = "stocks"
    allowed_domains = ["baidu.com"]
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        pass