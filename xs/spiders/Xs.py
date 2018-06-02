# -*- coding: utf-8 -*-
import scrapy
from xs.items import XsContentItem 
from scrapy.contrib.loader import ItemLoader
import json


class xsContentSpider(scrapy.Spider):
    name = 'xs_content'

    def start_requests(self):
        f = open('/yjdata/www/xs/20180524_211850/xs.json',encoding = 'utf-8')
        content = json.load(f)
        start_urls = []
        for url in content:
            yield scrapy.Request(url='https://www.booktxt.net'+ url['url'][0], callback=self.parse)

    def parse(self, response):
        items = ItemLoader(item=XsContentItem(),response=response)
        #章节标题
        items.add_xpath('title','//*[@id="wrapper"]/div[4]/div/div[2]/h1/text()')
        #正文
        items.add_xpath('text','//*[@id="content"]/text()')
        yield items.load_item()
            
