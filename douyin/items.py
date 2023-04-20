# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author = scrapy.Field()
    signature = scrapy.Field()
    desc = scrapy.Field()
    video_urls = scrapy.Field()
    video_paths = scrapy.Field()
    video_hash = scrapy.Field()
