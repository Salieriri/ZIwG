import scrapy


class PPE(scrapy.Spider):
    name = 'ppe'

    start_urls = [
        'https://www.ppe.pl/news.html',
    ]

    def parse(self, response, **kwargs):
        news_page_links = response.xpath("//div[@class='article-list-grid']/a")
        yield from response.follow_all(news_page_links, self.parse_news)

        next_page_link = response.xpath("//span[@class='pagination-button next ml-5']/a")
        yield from response.follow_all(next_page_link, self.parse)

    def parse_news(self, response):
        yield {
            'title': response.css('h1::text').get(),
            'date': response.xpath("//div[@class='author-with-avatar']/div/span/text()").get(),
            'text': response.xpath("//div[@class='content news']/p/text()").getall()
        }