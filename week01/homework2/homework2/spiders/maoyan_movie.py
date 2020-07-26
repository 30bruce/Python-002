import scrapy
from scrapy.selector import Selector
from homework2.items import Homework2Item


class MaoyanMovieSpider(scrapy.Spider):
    name = 'maoyan_movie'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        for movie in movies:
            title = movie.xpath("./div/span/text()")[0].extract()
            movie_type = movie.xpath("./div[2]/text()").extract()[-1].strip()
            plan_date = movie.xpath("./div[4]/text()").extract()[-1].strip()
            movie_item = Homework2Item()
            movie_item['title'] = title
            movie_item['movie_type'] = movie_type
            movie_item['plan_date'] = plan_date
            yield movie_item

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url, callback=self.parse)

