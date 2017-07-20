# -*- coding: utf-8 -*-
import scrapy


class MainSpiderSpider(scrapy.Spider):
    name = "main_spider"
    allowed_domains = ["sh.lianjia.com"]
    start_urls = ['http://sh.lianjia.com/ershoufang']

    def parse(self, response):

        pass
