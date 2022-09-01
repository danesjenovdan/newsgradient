from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime


class ZenitSpider(CustomSpider):

    name = 'zenit'

    allowed_domains = ['zenit.ba']
    start_urls = ['https://www.zenit.ba/']

    medium_id = 48

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'div.td-module-thumb > a',
    ]

    # ARTICLE PAGE
    news_title_class = 'h1.tdb-title-text::text'
    news_content_class = 'div.tdb_single_content > div.td-fix-index>p ::text'
    ignore_starts_words = []
    skip_after = ''
    date_element = 'time::attr(datetime)'

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return
        date = date_strings[0].split('+')[0]
        formated_date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
        return formated_date
