from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime


class VecernjiSpider(CustomSpider):

    name = 'vecernji'

    allowed_domains = ['vecernji.ba']
    start_urls = ['https://www.vecernji.ba/']

    medium_id = 46

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'div.card > a',
    ]

    # ARTICLE PAGE
    news_title_class = 'h1.article__title::text'
    news_content_class = 'div.article__body--main_content>p ::text'
    ignore_starts_words = []
    skip_after = ''
    date_element = 'meta[itemprop="datePublished"]::attr(content)'

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return
        date = date_strings[0].strip()
        formated_date = datetime.strptime(date, '%Y-%m-%d')
        return formated_date
