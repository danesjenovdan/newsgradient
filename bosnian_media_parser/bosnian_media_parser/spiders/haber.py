from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime


class HaberSpider(CustomSpider):

    name = 'haber'

    allowed_domains = ['haber.ba']
    start_urls = ['https://haber.ba/']

    medium_id = 1

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'a[rel="bookmark"]',
    ]

    # ARTICLE PAGE
    news_title_class = 'h1.post-title::text'
    news_content_class = 'div#content-main>p ::text'
    ignore_starts_words = []
    skip_after = ''
    date_element = 'meta[itemprop="dateModified"]::attr(content)'

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return
        date = date_strings[0]
        formated_date = datetime.strptime(date, '%Y-%m-%d')
        return formated_date
