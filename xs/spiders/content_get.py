# -*- coding: utf-8 -*-
import scrapy
from xs.items import XsItem 
from scrapy.contrib.loader import ItemLoader


class xsSpider(scrapy.Spider):
    name = 'xs'

    def start_requests(self):
        start_urls = ['https://www.booktxt.net/5_5622/']
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        count = 0
        items = ItemLoader(item=XsItem(),response=response)
        for content in response.xpath('//*[@id="list"]/dl/dd/a'):
                count = count+1
                i = ItemLoader(item=XsItem(),selector=content)
                #章节数
                i.add_value('chapter',count)
                #章节标题
                i.add_xpath('title','text()')
                #网址
                i.add_xpath('url','@href')
                yield i.load_item()
            

    
