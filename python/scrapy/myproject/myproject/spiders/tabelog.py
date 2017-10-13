from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from myproject.items import Restaurant

class TabelogSpider(CrawlSpider):
    name = "tabelog"
    allowed_domains = ["tabelog.com"]
    start_urls = (
        'http://tabelog.com/tokyo/rstLst/lunch/?LstCosT=2&RdoCosTp=1',
    )

    rules = [
        # for clawling pager
        Rule(LinkExtractor(allow=r'/\w+/rstLst/lunch/\d+/')),
        # for parsing detail page
        Rule(LinkExtractor(allow=r'/\w+/A\d+/A\d+/\d+/$'), callback='parse_restaurant'),
    ]


    def parse_restaurant(self, response):
        """
        レストランの詳細ページをパースする。
        """

        latitude, longitude = response.css(
            'img.js-map-lazyload::attr("data-original")').re(
            r'markers=.*?%7C([\d.]+),([\d.]+)')

        item = Restaurant(
            name = response.css('.display-name').xpath('string()').extract_first().strip(),
            address = response.css('.rstinfo-table__address').xpath('string()').extract_first().strip(),
            latitude = latitude,
            longitude = longitude,
            station = response.css('dt:contains("最寄り駅")+dd span::text').extract_first(),
            score = response.css('.tb-rating__val span').xpath('string()').extract_first(),
        )

        yield item

