import scrapy
import json
from homework01.items import Homework01Item


class IpproxyspiderSpider(scrapy.Spider):
    name = 'ipproxyspider'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']

    def parse(self, response):
        homework_item = Homework01Item()
        ip_data = json.loads(response.text)
        homework_item['origin_ip'] = ip_data.get('origin')
        yield homework_item
