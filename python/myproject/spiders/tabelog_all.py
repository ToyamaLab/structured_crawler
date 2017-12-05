from scrapy.spiders import SitemapSpider, CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy import Request
import json


from myproject.items import RestaurantJson

class TabelogAllSpider(SitemapSpider):
    name = "tabelog_all"
    allowed_domains = ["tabelog.com"]
    sitemap_urls = (
        'https://tabelog.com/sitemap.xml',
    )

    # sitemap_rules = [
    #     (r'/sitemap_pc_area1_rstlst_\d+.xml.gz$', 'parse_search_result'),
    # ]

    sitemap_rules = (
        ("https://tabelog.com/sitemap_pc_area1_rstlst_1.xml.gz", 'parse_search_result'),
        ("https://tabelog.com/sitemap_pc_area1_rstlst_2.xml.gz", 'parse_search_result'),
    )

    def parse_search_result(self, response):
        """
        地域ページからレストランページへのリンク
        https://tabelog.com/hokkaido/A0104/rstLst/cond04-00-03/RC999909/
        """

        restaurant_pages = response.css('a.list-rst__rst-name-target').extract()
        if restaurant_pages is not None:
            for page in restaurant_pages:
                yield Request(response.urljoin(page), callback=self.parse_restaurant)

    def parse_restaurant(self, response):

        """
        レストランページからJSON-LD
        :param response:
        :return:
        """

        restaurant_json = json.loads(response.css('script[type="application/ld+json"]').xpath('string()').extract_first())

        item = RestaurantJson(
            keyword = restaurant_json['name'],
            target = restaurant_json['@id']
        )

        yield item

