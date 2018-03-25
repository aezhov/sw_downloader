# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.files import FilesPipeline
from furl import furl
from .utils import format_dirname
import os


class SwDownloaderPipeline(FilesPipeline):
    """ Like standard FilesPipeLine
        but custom file_path
    """

    def file_path(self, request, response=None, info=None):
        super(SwDownloaderPipeline, self).file_path(request, response, info)
        url_parsed = furl(request.url)
        filename = os.path.basename(str(url_parsed.path))
        dirname = format_dirname(info.spider.year, info.spider.month,
                                 info.spider.resolution)
        path = os.path.join(dirname, filename)
        return path
