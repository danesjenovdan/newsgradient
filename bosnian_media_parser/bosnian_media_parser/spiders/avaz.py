from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime

class AvazSpider(CustomSpider):

    name = 'avaz'
    allowed_domains = ['avaz.ba']
    start_urls = ['https://avaz.ba/']

    medium_id = 51

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'artivle a',
        'div.sidbar-news a',
        'div.article-title a'
    ]

    # ARTICLE PAGE
    news_title_class = 'h1.title::text'
    news_content_class = 'div.artikal-text>p ::text'
    ignore_starts_words = []
    skip_after = None
    date_element = 'meta[property="article:published_time"]::attr(content)'

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



