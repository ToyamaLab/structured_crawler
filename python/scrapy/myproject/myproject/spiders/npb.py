import re

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from myproject.items import WixFileEntry

class NpbSpider(CrawlSpider):
    name = "npb"
    allowed_domains = ["npb.jp"]
    start_urls = (
        'http://npb.jp/bis/players/',
    )
    rules = [
        Rule(LinkExtractor(allow=r'/bis/teams/\w+'), callback='parse_players'),
    ]

    def parse_players(self, response):
        players = response.css('.rosterPlayer')
        for player in players:
            name_raw = player.css('td > a').xpath('string()').extract_first()
            url = response.urljoin(player.css('td > a::attr(href)').extract_first())
            print(type(name_raw))

            if name_raw:
                name = re.sub(r'[ \u3000\n\r]', '', name_raw)
            else:
                name = None
            # print("###########" + type(name_raw))
            # name = name_raw

            if name and url:
                entry = WixFileEntry(
                    keyword = name,
                    target = url,
                )
                yield entry






