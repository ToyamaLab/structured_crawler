import json
import re

from scrapy.spiders import SitemapSpider

from myproject.items import WixFileEntry

class EigaComSpider(SitemapSpider):
    name = "eiga_com"
    allowed_domains = ["eiga.com"]
    sitemap_urls = [
        'http://eiga.com/robots.txt',
    ]

    sitemap_follow = [
        r'movies_',
    ]

    sitemap_rules = [
        (r'/movie/[0-9]+/$', 'parse_movie'),
    ]

    def parse_movie(self, response):

        dirty_json = response.css('script[type="application/ld+json"]').xpath('string()').extract_first()
        movie_json = json.loads(self.remove_dirty_string(dirty_json))

        keyword = re.sub(r'[ \u3000\n\r]', '', self.remove_blackets(movie_json[0]['itemListElement'][2]['item']['name']))
        target = movie_json[0]['itemListElement'][2]['item']['@id']

        entry = WixFileEntry(
            keyword = keyword,
            target = target,
        )
        yield entry


    def remove_dirty_string(self, string):

        lstrip_string = r'^//<!\[CDATA\[\n'
        rstrip_string = r'\n//\]\]>$'

        string_cleaned = re.sub(rstrip_string, '', re.sub(lstrip_string, '', string))

        return string_cleaned

    def remove_blackets(self, string):

        lstrip_string = r'^映画「'
        rstrip_string = r'」$'

        string_cleaned = re.sub(rstrip_string, '', re.sub(lstrip_string, '', string))

        return string_cleaned





