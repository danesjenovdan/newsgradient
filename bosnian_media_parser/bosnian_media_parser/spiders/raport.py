from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime


class RaportSpider(CustomSpider):

    name = 'raport'

    allowed_domains = ['raport.ba']
    start_urls = ['https://raport.ba/']

    medium_id = 34

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'div.post-thumb a',
    ]

    # ARTICLE PAGE
    news_title_class = 'h1.entry-title::text'
    news_content_class = 'div.entry-content>p ::text'
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
        formated_date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
        return formated_date
