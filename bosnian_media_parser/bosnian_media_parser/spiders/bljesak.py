from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime

class N1infoSpider(CustomSpider):

    name = 'bljesak'

    allowed_domains = ['bljesak.info']
    start_urls = ['https://bljesak.info/']

    medium_id = 1

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'article > a',
    ]

    # ARTICLE PAGE
    news_title_class = 'h1.title::text'
    news_content_class = 'div.rte>p::text'
    ignore_starts_words = []
    skip_after = ''
    date_element = 'div.info>span::text'

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return
        date = date_strings[4].strip()
        formated_date = datetime.strptime(date, '%d. %m. %Y. u %H:%M')
        return formated_date



