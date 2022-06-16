import scrapy


class GryOnline(scrapy.Spider):
    name = 'gryonline'

    start_urls = [
        'https://www.gry-online.pl/newsroom/news/',
    ]

    def parse(self, response, **kwargs):
        news_page_links = response.xpath("//div[@class='lista lista-news']/div/a")
        yield from response.follow_all(news_page_links, self.parse_news)

        next_page_link = response.xpath("//div[@class='np-right']/a")
        yield from response.follow_all(next_page_link, self.parse)

    def parse_news(self, response):
        yield {
            'title': response.css('h1::text').get(),
            'date': response.css('span.a-d-data::text').get(),
            'text': response.css('article p::text').getall(),
        }
