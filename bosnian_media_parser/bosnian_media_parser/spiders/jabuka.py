from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime


class JabukaSpider(CustomSpider):

    name = 'jabuka'

    allowed_domains = ['jabuka.tv']
    start_urls = ['https://www.jabuka.tv/']

    medium_id = 23

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'div.vce-grid-text>a',
        'div.meta-image>a'
    ]

    # ARTICLE PAGE
    news_title_class = 'h1.entry-title::text'
    news_content_class = 'div.entry-content>p ::text'
    ignore_starts_words = []
    skip_after = ''
    date_element = 'div.date>span ::text'

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return
        date = date_strings[0].strip()

        return None
