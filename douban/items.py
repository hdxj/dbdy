# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DoubanItem(scrapy.Item):
    cover = scrapy.Field()
    id = scrapy.Field()
    is_released = scrapy.Field()
    m_url = scrapy.Field()
    orig_title = scrapy.Field()
    rating = scrapy.Field()
    rating_count = scrapy.Field()
    title = scrapy.Field()
    type = scrapy.Field()
    url = scrapy.Field()
    category = scrapy.Field()

class DoubanProfession(scrapy.Item):
    avatar = scrapy.Field()
    name = scrapy.Field()
    id = scrapy.Field()
    name_en = scrapy.Field()
    profession = scrapy.Field()
    type = scrapy.Field()
    url = scrapy.Field()
    category = scrapy.Field()

