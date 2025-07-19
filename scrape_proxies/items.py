import scrapy


class ScrapeProxiesItem(scrapy.Item):
    type = scrapy.Field()
    ip_address = scrapy.Field()
    port = scrapy.Field()
    country = scrapy.Field()
    city = scrapy.Field()
