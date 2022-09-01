from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime

import locale
locale.setlocale(locale.LC_ALL, "en_US.UTF-8")


class MojabanjalukaSpider(CustomSpider):

    name = 'mojabanjaluka'

    allowed_domains = ['mojabanjaluka.com']
    start_urls = ['http://mojabanjaluka.com/']

    medium_id = 26

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'div.single-blog>a',
        'div.pind-text>a',
        'div.text-bottom>a',
        'div.home-pind-text>a'
    ]

    # ARTICLE PAGE
    news_title_class = 'div.single_title>h2::text'
    news_content_class = 'div.body-text>p ::text'
    ignore_starts_words = []
    skip_after = ''
    date_element = 'div.single_title>label ::text'

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return
        date = date_strings[0].strip()
        formated_date = datetime.strptime(date, '%d. %b %Y')
        return formated_date
