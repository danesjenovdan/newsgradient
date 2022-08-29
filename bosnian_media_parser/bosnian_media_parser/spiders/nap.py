from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime


class NapSpider(CustomSpider):

    name = 'nap'

    allowed_domains = ['nap.ba']
    start_urls = ['https://nap.ba/']

    medium_id = 1

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'a',
    ]

    # ARTICLE PAGE
    news_title_class = 'div.title>h1::text'
    news_content_class = 'div.paragraf>p ::text'
    ignore_starts_words = []
    skip_after = 'Web stranicu novinske agencije Patria možete pratiti i putem aplikacije za'
    date_element = 'header>div>p>strong ::text'

    def parse_news(self, response):
        # parse just news links
        if '/news/' in response.url:
            return super().parse_news(response)

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return
        date = date_strings[1]
        formated_date = datetime.strptime(date, '%d.%m.%Y %H:%M:%S')
        return formated_date
