# -*- coding: utf-8 -*-

"""Console script for sw_downloader."""
import os
import sys
import datetime
import click
import re

os.environ.setdefault('SCRAPY_SETTINGS_MODULE',
                      'sw_downloader.sw_downloader.settings')

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

now = datetime.datetime.now()


def run_spider(year, month, resolution):
    process = CrawlerProcess(get_project_settings())
    process.crawl('smashingmagazine_spider', year=year,
                  month=month, resolution=resolution)
    process.start()


@click.command()
@click.option('--year', default=now.year)
@click.option('--month', default=now.month)
@click.option('--resolution', required=True,
              help=('resolution of wallpapers '
                    'in format like'
                    '1024x768, 800x600 etc.'))
def main(year, month, resolution):
    """Console script for sw_downloader."""
    click.echo("Smashing Magazine Wallpaper downloader")
    if not re.match(r"^\d+x\d+$", resolution):
        click.echo('   resolution option must be in format like'
                   '1024x768')
        sys.exit(2)

    run_spider(year=year, month=month, resolution=resolution)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
