from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime

class KlixSpider(CustomSpider):

    name = 'klix'
    allowed_domains = ['klix.ba']
    start_urls = ['https://www.klix.ba/']

    medium_id = 24

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'body>div>div.container div.relative>a',
    ]

    # ARTICLE PAGE
    news_title_class = 'h1.font-title::text'
    news_content_class = '#text ::text'
    ignore_starts_words = []
    skip_after = None
    date_element = 'meta[name="publish-date"]::attr(content)'

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return
        date = date_strings[0]
        formated_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
        return formated_date



