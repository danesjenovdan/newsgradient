from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime

class ZurnalSpider(CustomSpider):

    name = 'zurnal'

    allowed_domains = ['zurnal.info']
    start_urls = ['https://zurnal.info/']

    medium_id = 49

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'a.item',
    ]

    # ARTICLE PAGE
    news_title_class = 'div.caption>h1::text'
    news_content_class = 'div.body>p ::text'
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
        date = date_strings[0].strip()
        formated_date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        return formated_date



