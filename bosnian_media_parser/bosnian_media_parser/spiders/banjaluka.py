from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime


class BanjelukaSpider(CustomSpider):

    name = 'banjaluka'

    allowed_domains = ['banjaluka.com']
    start_urls = ['https://www.banjaluka.com/']

    medium_id = 4

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'article>a',
        'div.large-home>a',
        'div.medium-home>a',
    ]

    # ARTICLE PAGE
    news_title_class = 'h1.single-news-title::text'
    news_content_class = 'div.clanak p ::text'
    ignore_starts_words = []
    skip_after = ''
    date_element = 'p.datum ::text'

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return
        date = date_strings[0].replace('Objavljeno: ', '')
        formated_date = datetime.strptime(date, '%d. %m. %Y u %H:%Mh')
        return formated_date
