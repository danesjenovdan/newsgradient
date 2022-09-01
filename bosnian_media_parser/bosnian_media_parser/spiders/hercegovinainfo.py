from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime


class HercegovinaSpider(CustomSpider):

    name = 'hercegovina'

    allowed_domains = ['hercegovina.info']
    start_urls = ['https://www.hercegovina.info/']

    medium_id = 22

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'figure > a',
    ]

    # ARTICLE PAGE
    news_title_class = 'h1.post-title::text'
    news_content_class = 'div.entry-content>p::text'
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
        date = date_strings[0]

        formated_date = datetime.strptime(date, '%d.%m.%Y %H:%M')
        return formated_date
