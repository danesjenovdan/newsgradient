from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime

import json


class AloOnlineSpider(CustomSpider):

    name = 'aloonline'

    allowed_domains = ['aloonline.ba']
    start_urls = ['https://aloonline.ba/']

    medium_id = 1

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'div.news-box>a',
    ]

    # ARTICLE PAGE
    news_title_class = 'header.post-header>h1::text'
    news_content_class = 'div.the-content p ::text, div.the-content blockquote>div ::text'
    ignore_starts_words = []
    skip_after = ''
    date_element = 'script.yoast-schema-graph::text'

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return
        date = json.loads(date_strings[0])["@graph"][3]["datePublished"].split("+")[0]
        formated_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")
        return formated_date
