import scrapy


class Sport(scrapy.Spider):
    name = 'sport'

    start_urls = [
        'https://www.sport.pl/tenis/0,0.html'
    ]

    def parse(self, response, **kwargs):
        news_page_links = response.xpath("//li[@class='entry']/a")
        yield from response.follow_all(news_page_links, self.parse_news)

        next_page_link = response.xpath("//a[@class='next']")
        yield from response.follow_all(next_page_link, self.parse)

    def parse_news(self, response):
        yield {
            'title': response.xpath("//h1[@id='article_title']/text()").get(),
            'date':  response.xpath("//time").attrib['datetime'],
            'text': response.xpath("//p/text() | //p/*/text()").getall()
        }
