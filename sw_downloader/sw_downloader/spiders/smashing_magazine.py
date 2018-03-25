"""SmashingMagazine Wallpaper spider

Finds and downloading wallpapers on smashingmagazine.com with
specified parameters.

"""
import datetime
import logging

from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from furl import furl


class SmashingMagazineSpider(CrawlSpider):
    name = 'smashingmagazine_spider'
    start_urls = ['https://www.smashingmagazine.com/category/wallpapers/']
    rules = (
        Rule(
            LinkExtractor(allow=r"/wallpapers/"),
            callback='parse_posts_page'
        ),
    )

    def __init__(self, year, month, resolution, *args, **kwargs):
        super(SmashingMagazineSpider, self).__init__(*args, **kwargs)
        self.year = int(year)
        self.month = int(month)
        self.resolution = resolution

    def parse_wallpaper_page(self, response):
        links = response.css('.c-garfield-the-cat>ul>li>a::attr(href)'
                             ).extract()
        for link in links:
            if self.resolution in link and\
               ('.png' in link or '.jpg' in link):
                yield {'image_urls': [link]}

    def parse_posts_page(self, response):
        posts = response.css('.article--post,.tilted-featured-article')
        for post in posts:
            date_stamp = post.css('div>p>time::attr(datetime)').extract_first()
            date = datetime.datetime.strptime(date_stamp, "%Y-%m-%d")
            if date.month == self.month and date.year == self.year:
                path = post.css('h1>a::attr(href),h2>a::attr(href)'
                                ).extract_first()
                logging.info('found post at %s, path %s' % (date_stamp, path))
                parsed_url = furl(response.url)
                parsed_url.path = path
                yield Request(url=parsed_url.tostr(),
                              callback=self.parse_wallpaper_page)
