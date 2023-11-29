import scrapy
from cats.items import ImageScraperItem

import os

# demo https://unsplash.com/s/photos/cat

class CatSpider(scrapy.Spider):

    name = "cats"

    allowed_domains = ['unsplash.com']
    start_urls = ["https://unsplash.com/s/photos/cat-facing-camera"]
    max_pages = 1    

    def parse(self, response):

        image_url = response.css('div.MorZF img::attr(src)').getall()
        
        item = ImageScraperItem()
        for url in image_url:
            url += ".jpeg"
            item['image_urls'] = [url]  # Assuming image_url is the scraped image URL
            yield item