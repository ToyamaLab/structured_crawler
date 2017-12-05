import re

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from myproject.items import WixFileEntry

class GeinouproSpider(CrawlSpider):
    name = "geinoupro_blog"
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
            blog = entry.css('*').extract_first()
            span = entry.css('span').extract_first()
            if blog:
                blog_string = re.search(r'(?<=【ブログ】<a href=")(.+)(?=" target="_blank")', blog)
            else:
                blog_string = None
            if span:
                span_string = re.search(r'(?<=>)([^<]+)(?=（)', span)
            else:
                span_string = None

            if blog_string and span_string:
                name_raw = span_string.group(0)
                name = re.sub(r'[ \u3000\n\r]', '', name_raw)
                blog_url = blog_string.group(0)
                print(name, ":", blog_url)
                item = WixFileEntry(
                    keyword = name,
                    target = blog_url
                )
                yield item




