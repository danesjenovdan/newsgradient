from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime

class LogicnoSpider(CustomSpider):

    name = 'logicno'

    allowed_domains = ['logicno.com']
    start_urls = ['https://www.logicno.com/']

    medium_id = 1

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'a.w-grid-item-anchor',
        'span.post_title>a'
    ]

    # ARTICLE PAGE
    news_title_class = 'h1.post_title::text'
    news_content_class = 'div.post_content>p::text, div.post_content>h3>span ::text'
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
        date = date_strings[0].strip().split('+')[0]
        formated_date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
        return formated_date



