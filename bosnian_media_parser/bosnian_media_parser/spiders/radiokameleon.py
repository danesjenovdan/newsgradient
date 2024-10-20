from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime

import json

class RadiokameleonSpider(CustomSpider):

    name = 'radiokameleon'

    allowed_domains = ['radiokameleon.ba']
    start_urls = ['https://radiokameleon.ba/']

    medium_id = 35

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'div.grid-item > a',
        'li.post-item > a',
        'div.slide > a',

    ]

    # ARTICLE PAGE
    news_title_class = 'h1.post-title::text'
    news_content_class = 'div.entry-content > p::text'
    ignore_starts_words = []
    skip_after = ''
    date_element = 'script#tie-schema-json::text'

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return
        date = date_strings[0].strip()
        date = json.loads(date)['datePublished'].split('+')[0]
        formated_date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
        return formated_date



