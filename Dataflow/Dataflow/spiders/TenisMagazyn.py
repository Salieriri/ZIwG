import scrapy


class TenisMagazyn(scrapy.Spider):
    name = 'tenismagazyn'

    start_urls = [
        'https://tenismagazyn.pl/tenis-zawodniczy/'
    ]

    def parse(self, response, **kwargs):
        news_page_links = response.xpath("//article/a")
        yield from response.follow_all(news_page_links, self.parse_news)

        next_page_link = response.xpath("//a[@class='page-numbers next']")
        yield from response.follow_all(next_page_link, self.parse)

    def parse_news(self, response):
        yield {
            'title': response.xpath("//h1/text()").get(),
            'date':  response.xpath("//ul/li/a/span/text()").get(),
            'text': response.xpath("//h2[@class='has-medium-font-size']/*/text() | //p[not(@class)]/text()").getall()
        }