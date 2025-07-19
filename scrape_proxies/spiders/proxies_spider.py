import scrapy
import logging as log
from ..items import ScrapeProxiesItem


class ScrapeProxiesSpider(scrapy.Spider):
    name = "proxies"
    # start_urls = [
    #     "https://www.freeproxy.world/?type=https&anonymity=4&country=&speed=&port=&page=1"
    # ]

    def start_requests(self):
        total_pages = 556
        base = "https://www.freeproxy.world/?type=https&anonymity=4&country=&speed=&port=&page={}"
        for page in range(1, total_pages + 1):
            url = base.format(page)
            log.info(f"Requesting page {page}")
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        print(f"Scraping page: {response.url}")
        for row in response.css("tbody tr"):
            try:
                log.info(f"Scraping page: {response.url}")
                item = ScrapeProxiesItem()

                item["ip_address"] = row.css("td.show-ip-div::text").get(default="").strip()
                item["port"] = row.css("td:nth-child(2) a::text").get(default="").strip()
                item["country"] = row.css("span.table-country::text").get(default="").strip()
                item["city"] = row.css("td:nth-child(4)::text").get(default="").strip()
                item["type"] = row.css("td:nth-child(6) a::text").get(default="").strip().lower()
                yield item

            except Exception as e:
                log.info(f"Cannot scrape proxies: {e}")