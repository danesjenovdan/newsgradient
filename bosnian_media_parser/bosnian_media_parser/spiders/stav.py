from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime


class N1infoSpider(CustomSpider):

    name = 'stav'

    allowed_domains = ['stav.ba']
    start_urls = ['https://stav.ba/']

    medium_id = 1

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'a.news__link',
    ]

    # ARTICLE PAGE
    news_title_class = 'h1.news__heading::text'
    news_content_class = 'div.post-content>p ::text'
    ignore_starts_words = []
    skip_after = ''
    date_element = '.meta__data span::text'

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return
        date = date_strings[0].replace('|', '').strip()
        formated_date = datetime.strptime(date, '%d.%m.%Y.')
        return formated_date
