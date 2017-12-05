from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re

from myproject.items import SchemaUsage

class SchemaUsageSpider(CrawlSpider):
    name = "schema_usage"
    allowed_domains = ["schema.org"]
    start_urls = (
        'http://schema.org/docs/full.html',
    )

    rules = [
        # for clawling all
        Rule(LinkExtractor(), callback='parse_usage'),
    ]


    def parse_usage(self, response):
        """
        レストランの詳細ページをパースする。
        """

        usage_text = re.search(r'<div>Usage:.*</div>', response.xpath('//*[@id="mainContent"]').extract_first())
        if usage_text is None:
            usage = ""
        else:
            usage = usage_text.group(0)

        item = SchemaUsage(
            schema_type = response.css('.page-title').xpath('string()').extract_first(),
            usage = usage
        )

        yield item

