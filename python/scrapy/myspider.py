import scrapy


class BlogSpider(scrapy.Spider):
    name = 'blogspider'

    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        """
        トップページからカテゴリページをたどる
        :param response: 
        :return: 
        """

        for url in response.css('ul li a::attr("href")').re('.*/category/.*'):
            yield scrapy.Request(response.urljoin(url), self.parse_titles)

    def parse_titles(self, response):
        """
        カテゴリページから投稿のタイトルを抽出
        :param response: 
        :return: 
        """
        for post_title in response.css('div.entries > ul > li a::text').extract():
            yield {'title': post_title}

