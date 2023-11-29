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




        # image_url = response.css('div.MorZF img::attr(src)').get()
        
        # if image_url:
        #     # Get the image data from the URL
        #     image_data = response.follow(image_url).body

        #     if image_data:
        #         # Specify the folder path to save the image
        #         folder_path = '/Users/chenc/cats'  # Change this to your desired folder name
        #         os.makedirs(folder_path, exist_ok=True)

        #         # Specify the file name (you can modify this)
        #         filename = os.path.join(folder_path, 'cat_image.jpg')

        #         # Save the image to the specified folder
        #         with open(filename, 'wb') as f:
        #             f.write(image_data)

        #         # Print a message or log the saved file name
        #         self.log(f'Saved file {filename}')
        #     else:
        #             self.log('Image data is empty.')
        
        
        
    #     obj = ImageScraperItem()
    #     if response.status == 200:
    #     #This query only returns the first image
    #         #rel_img_urls = response.css('img').getall()
    #         image_url = response.css('div.MorZF img::attr(src)').get()
    #         #This returns all other images
    #         # rel_secondary_urls = response.css('img').xpath('@data-original').getall()
    #         # rel_img_urls.extend(rel_secondary_urls)
    #         #Finding number of pages
    #         # number_of_pages = response.xpath('//a[@class="loadmore page-number"]/text()').getall()
    #         obj['image_urls'] = self.url_join(image_url, response)
    #         yield obj

    # def url_join(self, rel_img_urls, response):
    #     urls = [response.urljoin(x) for x in rel_img_urls]
    #     return urls
        
        






    #     #images_urls
    #     obj = ImageScraperItem()
    #     if response.status == 200:
    #     #This query only returns the first image
    #         rel_img_urls = response.css('div.MorZF img').getall()
    #         #This returns all other images
    #         rel_secondary_urls = response.css('img').xpath('@data-original').getall()
    #         rel_img_urls.extend(rel_secondary_urls)
    #         #Finding number of pages
    #         number_of_pages = response.xpath('//a[@class="loadmore page-number"]/text()').getall()
    #         obj['image_urls'] = self.url_join(rel_img_urls, response)
    #         yield obj
    #         #If the number_of_pages length is 1, then it means that there is only one page extra
    #         if len(number_of_pages) == 1:
    #             self.max_pages = (number_of_pages[0])
    #         else:
    #         #finding the max
    #             number_of_pages = [int(x) for x in number_of_pages]
    #             self.max_pages = str(max(number_of_pages))
    #         # print(self.max_pages)
    #     # updating link
    #     next_page = self.base_link + '/page/' + str(self.max_pages)
    #     # callback for the next page
    #     yield scrapy.Request(next_page, callback=self.parse)
    # # converting relative to absolute URLS
    # def url_join(self, rel_img_urls, response):
    #     urls = [response.urljoin(x) for x in rel_img_urls]
    #     return urls