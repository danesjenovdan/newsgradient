from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime

class PoskokSpider(CustomSpider):

    name = 'poskok'

    allowed_domains = ['poskok.info']
    start_urls = ['https://poskok.info/']

    medium_id = 1

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'a[rel="bookmark"]',
    ]

    # ARTICLE PAGE
    news_title_class = 'div.post>h1::text'
    news_content_class = 'div.post>div.entry>div>p::text, div.post>div.entry>div>blockquote>p::text'
    ignore_starts_words = []
    skip_after = ''
    date_element = 'meta[property="og:article:published_time"]::attr(content)'

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return
        date = date_strings[0].strip().split('+')[0]
        formated_date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        return formated_date



