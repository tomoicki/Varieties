import scrapy
from ..items import ImgScraperItem


class QuotesSpider(scrapy.Spider):
    name = "img"
    start_urls = [
    ]

    def parse(self, response):
        each_gal = response.xpath('//a[@class="list clth"]/@href').getall()
        yield from response.follow_all(each_gal, self.browse_all_galeries)

    def browse_all_galeries(self, response):
        all_galeries = response.xpath('//a[@class="list_model clth"]/@href').getall()
        yield from response.follow_all(all_galeries, self.browse_each_pic)

    def browse_each_pic(self, response):
        all_imgs = response.xpath('//a[@class="clth"]/@href').getall()
        yield from response.follow_all(all_imgs, self.download_pic)

    def download_pic(self, response):
        get_pic = response.css("img").attrib['src']
        base = list(response.url)
        for i in range(len(base) - 1, 0, -1):
            if base[i] == '/':
                break
            del(base[i])
        base_link = ''.join(base)
        repaired_path = base_link + get_pic
        image = ImgScraperItem()
        image["image_urls"] = [repaired_path]
        yield image
