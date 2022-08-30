from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime

class OslobodjenjeSpider(CustomSpider):

    name = 'oslobodjenje'

    allowed_domains = ['oslobodjenje.ba']
    start_urls = ['https://www.oslobodjenje.ba/']

    medium_id = 1

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'article > a',
    ]

    # ARTICLE PAGE
    news_title_class = 'h1.item__title::text'
    news_content_class = 'div.itemFullText ::text'
    ignore_starts_words = []
    skip_after = 'Pratite nas na'
    date_element = 'span.card__time::text'

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return
        date = date_strings[0]
        formated_date = datetime.strptime(date, '%d/%m/%Y u %H:%M h')
        return formated_date



