from bosnian_media_parser.spiders.spider import CustomSpider
from datetime import datetime
class BiscaniSpider(CustomSpider):

    name = 'biscani'
    allowed_domains = ['biscani.net']
    start_urls = ['https://www.biscani.net/']

    medium_id = 1

    # HOMEPAGE
    allowed_home_page_div_classes = [
        '.td-module-thumb>a'
    ]

    # ARTICLE PAGE
    news_title_class = 'h1.entry-title::text'
    news_content_class = '.td-post-content ::text'
    ignore_starts_words = [
        'var mpi_wi',
        'var td_screen_width',
        'var mpn_wi=',
        '(adsbygoogle']
    skip_after = ''
    date_element = 'time.entry-date::attr(datetime)'

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return
        date = date_strings[0].split('+')[0]
        formated_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")
        return formated_date
