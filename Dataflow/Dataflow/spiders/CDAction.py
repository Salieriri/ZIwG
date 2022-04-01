import scrapy


class CDAction(scrapy.Spider):
    name = 'cdaction'

    def parse(self, response, **kwargs):
        pass