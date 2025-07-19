import logging as log
from .items import ScrapeProxiesItem
from scrapy.exceptions import DropItem
import json

class ScrapeProxiesPipeline:
    
    def open_spider(self, spider):
        self.proxies_file = open('proxies.jsonl', 'w', encoding='utf-8')
        log.info("File opened")

    def close_spider(self, spider):
        self.proxies_file.close()
        log.info("File closed")

    def process_item(self, item, spider):
        log.info("Item processing")

        if isinstance(item, ScrapeProxiesItem):
            if not item.get("ip_address") or not item.get("port"):
                raise DropItem("Missing ip or port in quote")
            
            line = json.dumps(dict(item), ensure_ascii=False)
            self.proxies_file.write(line + "\n")
            return item

        else:
            raise DropItem(f"Unknown item type: {type(item)}")
