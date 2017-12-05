import re

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from myproject.items import WixFileEntry

class GeinouproSpider(CrawlSpider):
    name = "geinoupro_site"
    allowed_domains = ["geinoupro.com"]
    start_urls = ['http://geinoupro.com/profil.html']

    rules = [
        # for clawling all
        Rule(LinkExtractor(), callback='parse'),
    ]

    def parse(self, response):

        entries = response.css('#main-contents > ul > li')
        print(type(entries))
        for entry in entries:
            site = entry.css('*').extract_first()
            span = entry.css('span').extract_first()
            if site:
                site_string = re.search(r'(?<=【サイト】<a href=")(.+)(?=" target="_blank")', site)
            else:
                site_string = None
            if span:
                span_string = re.search(r'(?<=>)([^<]+)(?=（)', span)
            else:
                span_string = None

            if site_string and span_string:
                name_raw = span_string.group(0)
                name = re.sub(r'[ \u3000\n\r]', '', name_raw)
                site_url = site_string.group(0)
                # print(name, ":", site_url)
                item = WixFileEntry(
                    keyword = name,
                    target = site_url
                )
                yield item






