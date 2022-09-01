from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime

class TacnoSpider(CustomSpider):

    name = 'tacno'

    allowed_domains = ['tacno.net']
    start_urls = ['https://www.tacno.net/']

    medium_id = 1

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'div.article-content>h4>a',
        'div.article-content>h2>a',
    ]

    # ARTICLE PAGE
    news_title_class = 'div.article-title>h1::text'
    news_content_class = 'div.paragraph-row>div.column9>p ::text'
    ignore_starts_words = ['foto:', 'Foto:']
    skip_after = ''
    date_element = 'meta[property="article:published_time"]::attr(content)'

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



