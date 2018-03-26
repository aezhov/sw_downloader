""" Common helper functions """

import datetime


def format_dirname(year, month, resolution):
    date_part = datetime.datetime(month=month, year=year, day=1).strftime('%Y-%B')
    return "{date_part}-{resolution}".format(date_part=date_part,
                                             resolution=resolution)
