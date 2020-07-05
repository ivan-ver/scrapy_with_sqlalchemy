import scrapy
from scrapy.spiders import Rule, Spider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from web_scraper.items import Books

class Spider1(Spider):
    name = 'spider1'
    start_urls = ['https://readrate.com/rus/ratings/top100']

    # rules = (
    #     Rule(LinkExtractor(allow=('/book/')), callback='parse_item'),
    # )

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        urls = LinkExtractor(allow=('/rus/books/')).extract_links(response)
        for url in urls[85:]:
            yield scrapy.Request(url=url.url, callback=self.local_parse)

    def local_parse(self, response):
        book = Books()
        title = response.xpath("//div[@class='header']/h1/text()").get()
        author = response.xpath("//li[@class='contributor item']/a/text()").get()
        print(title)
        print(author)
        book['title'] = title
        book['author'] = author
        yield book







