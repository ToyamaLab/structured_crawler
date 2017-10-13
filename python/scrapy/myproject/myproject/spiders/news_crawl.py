from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from myproject.items import Headline

class NewsCrawlSpider(CrawlSpider):
    name = "news_crawl"
    allowed_domains = ["news.yahoo.co.jp"]
    start_urls = ['http://news.yahoo.co.jp/']

    rules = (
        Rule(LinkExtractor(allow=r'/pickup/\d+$'), callback='parse_topics'),
    )


    def parse_topics(self, response):
        item = Headline()
        item['title'] = response.css('.newsTitle ::text').extract_first()
        item['body'] = response.css('.hbody').xpath('string()').extract_first()
        yield item