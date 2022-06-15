import scrapy


class PrzegladSportowy(scrapy.Spider):
    name = 'przeglad'

    start_urls = [
        'https://przegladsportowy.onet.pl/tenis',
    ]

    def parse(self, response, **kwargs):
        pass

    def parse_news(self, response):
        pass
