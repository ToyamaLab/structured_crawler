# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Headline(scrapy.Item):
    title = scrapy.Field()
    body = scrapy.Field()

class Restaurant(scrapy.Item):
    """
    食べログのレストラン情報。
    """

    name = scrapy.Field()
    address = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    station = scrapy.Field()
    score = scrapy.Field()

class RestaurantJson(scrapy.Item):
    """
    http://schema.org/Restaurant
    """

    keyword = scrapy.Field()
    target = scrapy.Field()


class SchemaUsage(scrapy.Item):
    """
    http://schema.org/
    """

    schema_type = scrapy.Field()
    usage = scrapy.Field()

