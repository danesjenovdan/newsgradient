from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime

class PressmediabihSpider(CustomSpider):

    name = 'pressmediabih'

    allowed_domains = ['pressmediabih.com']
    start_urls = ['https://pressmediabih.com/']

    medium_id = 1

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'div.text-block>h5>a',
        'div.sidebar-text>a',
    ]

    # ARTICLE PAGE
    news_title_class = 'h1.entry-title::text'
    news_content_class = 'div.entry-content>p ::text'
    ignore_starts_words = []
    skip_after = ''
    date_element = 'span.datum ::text'

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return
        date = date_strings[0].split(',')[1].strip()
        formated_date = datetime.strptime(date, '%d.%m.%Y.')
        return formated_date



