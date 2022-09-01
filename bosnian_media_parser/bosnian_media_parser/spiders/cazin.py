from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime

class CazinSpider(CustomSpider):

    name = 'cazin'

    allowed_domains = ['cazin.net']
    start_urls = ['https://www.cazin.net/']

    medium_id = 12

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'div.field__item > a',
        'div.post-image > a'
    ]

    # ARTICLE PAGE
    news_title_class = 'h1.post-title > span::text'
    news_content_class = 'div.paragraph__column ::text'
    ignore_starts_words = []
    skip_after = None
    date_element = 'span.post-created::text'

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return
        date = ''.join(date_strings[0].split('|')[:2]).strip()
        formated_date = datetime.strptime(date, '%d.%m.%Y  %H:%M')
        return formated_date



