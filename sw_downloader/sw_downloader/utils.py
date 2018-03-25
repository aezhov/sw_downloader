""" Common helper functions """

import datetime

def format_dirname(year, month, resolution):
    date_part = datetime.datetime(month=2, year=2018, day=1).strftime('%Y-%B') 
    return "{date_part}-{resolution}".format(date_part=date_part,
                                            resolution=resolution)
