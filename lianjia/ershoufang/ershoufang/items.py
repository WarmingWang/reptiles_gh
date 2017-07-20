# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ErshoufangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field          #标题，房源名称
    title_url=scrapy.Field      #房源链接
    apt_type=scrapy.Field       #房型
    area=scrapy.Field           #面积
    price_total = scrapy.Field  #总价
    price_per = scrapy.Field    #每平米单价
    floor=scrapy.Field          #楼层
    direction=scrapy.Field      #朝向
    community=scrapy.Field      #小区
    community_url=scrapy.Field  #小区链接
    district=scrapy.Field       #所属区，浦东、杨浦
    town=scrapy.Field           #镇
    year=scrapy.Field           #建造年份
    apt_id=scrapy.Field         #房源ID

