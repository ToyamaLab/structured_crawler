from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import json

from myproject.items import WixFileEntry

class TabelogSpider(CrawlSpider):
    name = "tabelog"
    allowed_domains = ["tabelog.com"]
    start_urls = (
        'http://tabelog.com/sitemap/tokyo/',
    )

    rules = [
        # for clawling pager
        Rule(LinkExtractor(allow=r'/sitemap/tokyo/A\d+-A\d+/$')),
        Rule(LinkExtractor(allow=r'/sitemap/tokyo/A\d+-A\d+/\w+/$')),
        Rule(LinkExtractor(allow=r'/sitemap/tokyo/A\d+-A\d+/\w+/?PG=\d+$')),
        # for parsing detail page
        Rule(LinkExtractor(allow=r'/\w+/A\d+/A\d+/\d+/$'), callback='parse_restaurant'),
    ]


    def parse_restaurant(self, response):
        """
        レストランの詳細ページからJSON-LDをパースする。
        """

        restaurant_json = json.loads(response.css('script[type="application/ld+json"]').xpath('string()').extract_first())

        item = WixFileEntry(
            keyword = restaurant_json['name'],
            target = restaurant_json['@id']
        )

        yield item