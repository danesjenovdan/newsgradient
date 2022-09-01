from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime


class BlportalSpider(CustomSpider):

    name = 'blportal'

    allowed_domains = ['bl-portal.com']
    start_urls = ['https://www.bl-portal.com/']

    medium_id = 1

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'div.post-img-wrap>a',
    ]

    # ARTICLE PAGE
    news_title_class = 'h1.entry-title::text'
    news_content_class = 'div.entry-content>p ::text'
    ignore_starts_words = []
    skip_after = ''
    date_element = 'div.date>a::text'

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return
        date = date_strings[0].strip()
        formated_date = datetime.strptime(date, '%d/%m/%Y %H:%M')
        return formated_date
