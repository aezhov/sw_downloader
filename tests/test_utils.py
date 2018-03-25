from sw_downloader.sw_downloader import utils


def test_format_filename():
    formatted = utils.format_dirname(month=2, year=2018, resolution='1024x768')
    assert formatted == '2018-February-1024x768'
