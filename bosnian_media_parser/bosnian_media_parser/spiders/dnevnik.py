from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime

import re

class DnevnikSpider(CustomSpider):

    name = 'dnevnik'

    allowed_domains = ['dnevnik.ba']
    start_urls = ['https://www.dnevnik.ba/']

    medium_id = 14

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'article > a',
    ]

    # ARTICLE PAGE
    news_title_class = 'h1.item__title::text'
    news_content_class = 'div.itemFullText>p::text'
    ignore_starts_words = []
    skip_after = ''
    date_element = 'span.card__time::text'

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return
        date = date_strings[0].strip().replace(u'\xa0', u'').replace('/','')
        formated_date = datetime.strptime(date, '%d.%m.%Y., %H:%Mh')
        return formated_date
