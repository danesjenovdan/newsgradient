from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime

class FederalnaSpider(CustomSpider):

    name = 'federalna'

    allowed_domains = ['federalna.ba']
    start_urls = ['https://federalna.ba/']

    medium_id = 1

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'div.carousel-item > a',
        'div.card > div > a',
        'div.card-body > h5.card-title > a',
    ]

    # ARTICLE PAGE
    news_title_class = 'div.article h1::text'
    news_content_class = 'div.lead ::text'
    ignore_starts_words = []
    skip_after = 'Pratite nas na'
    date_element = 'div.article-meta > span ::text'

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return
        date = ' '.join(date_strings[0].strip().split(' ')[1:])
        formated_date = datetime.strptime(date, '%d.%m.%Y. %H:%M')
        return formated_date



