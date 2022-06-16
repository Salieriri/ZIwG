import scrapy


class SportoweFakty(scrapy.Spider):
    name = 'sportowefakty'

    start_urls = [
        'https://sportowefakty.wp.pl/tenis/polski-tenis'
    ]

    def parse(self, response, **kwargs):
        news_page_links = response.xpath("//span[@class='h4 streamshort__title']/a")
        yield from response.follow_all(news_page_links, self.parse_news)

        next_page_link = response.xpath("//li[@class='pagination__arrow pagination__arrow--right go']/a")
        yield from response.follow_all(next_page_link, self.parse)

    def parse_news(self, response):
        yield {
            'title': response.xpath("//h1/text()").get(),
            'date': response.xpath("//time[@class='indicator__time']").attrib['datetime'],
            'text': response.xpath("//article/text() | //article/p/*/text() | //article/p/text()").getall()
        }