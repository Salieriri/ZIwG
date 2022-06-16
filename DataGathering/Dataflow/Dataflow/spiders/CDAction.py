import scrapy


class CDAction(scrapy.Spider):
    name = 'cdaction'
    url = 'https://cdaction.pl/newsy?strona='
    start_urls = [
        'https://cdaction.pl/newsy'
    ]

    def parse(self, response, **kwargs):
        news_page_links = response.xpath("/html/body/div[1]/main/section[2]/div[4]/div[1]/div")
        yield from response.follow_all(news_page_links, self.parse_news)

        for page in range(2, 60):
            yield from response.follow_all(self.url + str(page), self.parse)

    def parse_news(self, response):
        yield {
            'title': response.xpath("//h1/text()").get(),
            'date': response.xpath("/html/body/div[1]/main/section[1]/div[2]/div/div[3]/span[1]/text()").get(),
            'text': response.xpath("//p/text() | //p/*/text() | //p/*/b/text()").getall()
        }