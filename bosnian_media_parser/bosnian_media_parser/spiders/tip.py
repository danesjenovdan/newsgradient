from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime

class TipSpider(CustomSpider):

    name = 'tip'

    allowed_domains = ['tip.ba']
    start_urls = ['https://tip.ba/']

    medium_id = 1

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'section#grid_4x4>a',
        'h2.posttitle>a'
    ]

    # ARTICLE PAGE
    news_title_class = 'h1.entry-title::text'
    news_content_class = 'div.post>p ::text'
    ignore_starts_words = []
    skip_after = ''
    date_element = 'span#post-date::text'

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return
        date = date_strings[0].strip()
        formated_date = datetime.strptime(date, '%d.%m.%Y %H:%M')
        return formated_date



