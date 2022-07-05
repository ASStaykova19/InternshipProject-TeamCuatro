from itertools import product
import scrapy


class GovSpider(scrapy.Spider):
    name = 'gov'
    start_urls = ['https://gov.bg/bg/prestsentar/novini/']

    def parse(self,response):
        for products in response.css('div.item.no-padding'):
            yield {
                'title':products.css("div.col-lg-7 a::text").get(),
                'link': products.css("div.col-lg-7 a::attr(href)").get(),
            } 



        next_page = response.css('a.frontend.paginator.next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

         