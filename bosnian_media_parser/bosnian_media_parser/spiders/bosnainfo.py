from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime


class BosnaInfoSpider(CustomSpider):

    name = 'bosnainfo'

    allowed_domains = ['bosnainfo.ba']
    start_urls = ['https://bosnainfo.ba/']

    medium_id = 10

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'article>a',
    ]

    # ARTICLE PAGE
    news_title_class = 'div.article__top-content>h1::text'
    news_content_class = 'div.article__content>p ::text'
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
        formated_date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        return formated_date
