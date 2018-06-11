# -*- coding: utf-8 -*-
import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs-title'
    allowed_domains = ['craigslist.org']
    start_urls = ['https://portland.craigslist.org/search/jjj?query=data+analyst/']

    def parse(self, response):
        titles = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()
        #print(titles)
        for title in titles:
            yield {'Title': title}
