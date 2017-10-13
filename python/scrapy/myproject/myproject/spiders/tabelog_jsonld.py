from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import json


from myproject.items import RestaurantJson

class TabelogJsonldSpider(CrawlSpider):
    name = "tabelog_jsonld"
    allowed_domains = ["tabelog.com"]
    start_urls = (
        'http://tabelog.com/tokyo/rstLst/lunch/?LstCosT=2&RdoCosTp=1',
    )

    rules = [
        # for clawling pager
        Rule(LinkExtractor(allow=r'/\w+/rstLst/lunch/\d/')),
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

