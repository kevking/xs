# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.loader.processors import MapCompose,TakeFirst

class XsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    chapter = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()

class XsContentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    text = scrapy.Field(
        input_processor = MapCompose(lambda x:x.strip())
    )
