# -*- coding: utf-8 -*-

"""Main module."""

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from sw_downloader.spiders.smashing_magazine import SmashingMagazineSpider


def run_spider(year, month, resolution):
    process = CrawlerProcess(get_project_settings())
    process.crawl('smashingmagazine_spider', year=year, month=month, resolution=resoluion)
    process.start()
