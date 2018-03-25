# -*- coding: utf-8 -*-

# Scrapy settings for sw_downloader project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'sw_downloader'

SPIDER_MODULES = ['sw_downloader.sw_downloader.spiders']
NEWSPIDER_MODULE = 'sw_downloader.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'sw_downloader.sw_downloader.pipelines.SwDownloaderPipeline': 300,
}

FILES_STORE = './'
