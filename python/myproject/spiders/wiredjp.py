from scrapy.spiders import SitemapSpider


class WiredjpSpider(SitemapSpider):
    name = 'wiredjp'
    allowed_domains = ["wired.jp"]

    sitemap_urls = [
        "http://wired.jp/sitemap.xml",
    ]

    sitemap_follow = [
        r'post-2016-12',
    ]

    sitemap_rules = [
        (r'/2016/\d\d/\d\d/', 'parse_post'),
    ]

    def parse_post(self, response):
        yield {
            'title': response.css('h1.post-title::text').extract_first(),
        }