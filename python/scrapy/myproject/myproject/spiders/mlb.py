import re
import json

from spiders.microdata import microdata

from scrapy.spiders import SitemapSpider
from scrapy.linkextractors import LinkExtractor

from myproject.items import WixFileEntry

class MlbSpider(SitemapSpider):
    name = "mlb"
    allowed_domains = ["m.mlb.com"]
    sitemap_urls = [
        'http://m.mlb.com/robots.txt',
    ]

    sitemap_rules = [
        (r'/player/[0-9]+/.+$', 'parse_players'),
    ]

    def parse_players(self, response):
        jsons_law = response.css('[type="application/ld+json"]').xpath('string()').extract()

        for json_law in jsons_law:
            player = json.loads(json_law)

            if player['@type'] == 'Person':
                entry = WixFileEntry(
                    keyword=player['name'],
                    target=response.url,
                )
                yield entry


