import scrapy


class EurogamerSpider(scrapy.Spider):
    name = 'eurogamer'

    start_urls = [
        'https://www.eurogamer.pl/archive',
    ]

    def parse(self, response, **kwargs):
        news_page_links = response.xpath("//div[@class='compact-archive']/div/a")
        yield from response.follow_all(news_page_links, self.parse_news)

        next_page_link = response.xpath("//a[@class='button next']")
        yield from response.follow_all(next_page_link, self.parse)

    def parse_news(self, response):
        yield {
            'title': response.css('h1.title::text').get(),
            'date': response.css('header div.metadata div.date span').attrib['content'],
            'text': response.css('div.body p::text').getall(),
        }
