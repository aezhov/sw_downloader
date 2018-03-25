import requests

from scrapy.http import HtmlResponse
from sw_downloader.sw_downloader.spiders.smashing_magazine \
    import SmashingMagazineSpider


class TestSmashingMagazineSpider:

    def test_ruleset(self):
        url = ('https://www.smashingmagazine.com/category/wallpapers')
        response = requests.get(url)
        spider = SmashingMagazineSpider(year=2018, month=2,
                                        resolution='1024x768')
        scrapy_response = HtmlResponse(body=response.content, url=url)
        links_gen = spider._requests_to_follow(scrapy_response)
        links = list(links_gen)
        assert len(links) == 3

    def test_image_link_extraction(self):
        url = ('https://www.smashingmagazine.com/'
               '2018/01/desktop-wallpaper-'
               'calendars-february-2018/')

        spider = SmashingMagazineSpider(year=2018, month=1,
                                        resolution='1024x768')
        response = requests.get(url)
        scrapy_response = HtmlResponse(body=response.content, url=url)
        items_gen = spider.parse_wallpaper_page(scrapy_response)
        items = list(items_gen)
        assert len(items) == 26
        for item in items:
            assert '1024x768.jpg' in item['image_urls'][0] or \
                   '1024x768.png' in item['image_urls'][0]

    def test_extract_posts(self):
        url = ('https://www.smashingmagazine.com/category/wallpapers')
        spider = SmashingMagazineSpider(year=2018, month=2,
                                        resolution='1024x768')
        response = requests.get(url)
        scrapy_response = HtmlResponse(body=response.content, url=url)
        posts_gen = spider.parse_posts_page(scrapy_response)
        posts = list(posts_gen)
        assert len(posts) == 2
