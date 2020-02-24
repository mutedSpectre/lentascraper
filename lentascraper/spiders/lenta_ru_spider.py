from lentascraper.items import LentascraperItem

from datetime import datetime
import scrapy
from urllib.parse import urljoin

class LentaRuSpider(scrapy.Spider):
    name = "lentascraper"
    
    def start_requests(self):
        url = 'https://lenta.ru/'

        rubric = getattr(self, 'rubric', None)
        date = getattr(self, 'date', None)

        if rubric is not None and date is not None:
            url = url + 'rubrics/' + rubric + '/' + date
        elif rubric is None and date is not None:
            url = url + date
        elif rubric is not None and date is None:
            url = url + 'rubrics/' + rubric 
        else: 
            url = url + datetime.today().strftime('%Y/%m/%d')

        yield scrapy.Request(url, self.parse)


    def parse(self, response):
        for post_link in response.xpath('//div[@class="titles"]/h3/a/@href').extract():
            url = urljoin(response.url, post_link)
            yield response.follow(url, callback=self.parse_post)


    def parse_post(self, response):
        item = LentascraperItem()

        item['url'] = response.url

        title = response.xpath('//div[@class="b-topic__header js-topic__header"]/h1/text()').extract()
        item['title'] = title

        body = response.xpath('//div[@class="b-text clearfix js-topic__text"]//p/text()').extract()
        item['body'] = body

        date = response.xpath('//time[@class="g-date"]/@datetime').extract()
        item['date'] = date

        yield item
