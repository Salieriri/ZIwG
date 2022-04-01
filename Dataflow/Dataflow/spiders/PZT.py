import scrapy


class PZT(scrapy.Spider):
    name = 'pzt'
    dates = []

    start_urls = [
        'https://www.pzt.pl/2_154/aktualnosci.aspx',
    ]

    def parse(self, response, **kwargs):
        news_page_links = response.xpath("//div[@class='mMainBoxTxt']/div/div/div/a")
        self.dates.extend(response.xpath("//div[@class='listNewsBoxDatePublic']/text()").getall())
        yield from response.follow_all(news_page_links, self.parse_news)

        next_page_link = response.xpath("//div[@class='NewsPager']/div/a")
        yield from response.follow_all(next_page_link, self.parse)

    def parse_news(self, response):
        yield {
            'title': response.xpath("//h2/text()").get(),
            'date': self.dates.pop(0) if len(self.dates) else None,
            'text': response.xpath("//div[@class='m_contMainBoxCont2']/text()").getall()
        }
