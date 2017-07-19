# -*- coding: utf-8 -*-

import scrapy
from sc_test.items import ScTestItem

class DmozSpider(scrapy.Spider):
    name='dmoz'
    allowed_donmians=['dmoztools.net']
    start_urls=[
        "http://www.dmoztools.net/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoztools.net/Computers/Programming/Languages/Python/Resources/"
    ]

    # def parse(self,response):
    #     filename=response.url.split("/")[-2]
    #     with open(filename,'wb') as f:
    #         f.write(response.body)

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            item=ScTestItem()
            item['title']=sel.xpath('a/text()').extract()
            item['link']=sel.xpath('a/@href').extract()
            item['desc']=sel.xpath('text()').extract()
            yield item
            # title=sel.xpath('a.text()').extract()
            # link=sel.xpath('a/@href').extract()
            # desc=sel.xpath('text()').extract()
            # print(title,link, desc)



