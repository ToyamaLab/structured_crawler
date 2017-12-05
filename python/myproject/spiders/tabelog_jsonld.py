from scrapy.spiders import CrawlSpider, SitemapSpider, Rule
from scrapy.linkextractors import LinkExtractor
import json


from myproject.items import RestaurantJson

class TabelogJsonldSpider(CrawlSpider):
    name = "tabelog_jsonld"
    allowed_domains = ["tabelog.com"]

    start_urls = [
        'https://tabelog.com/sitemap',
    ]

    sitemap_rules = [
        Rule(LinkExtractor(allow=r'/sitemap/\w+$/'))
    ]


    rules = [
        # for parsing detail page
        Rule(LinkExtractor(allow=r'/\w+/A\d+/A\d+/\d+/$'), callback='parse_restaurant'),
    ]


    def parse_restaurant(self, response):
        """
        レストランの詳細ページからJSON-LDをパースする。
        """

        restaurant_json = json.loads(response.css('script[type="application/ld+json"]').xpath('string()').extract_first())

        item = RestaurantJson(
            keyword = restaurant_json['name'],
            target = restaurant_json['@id']
        )

        yield item

