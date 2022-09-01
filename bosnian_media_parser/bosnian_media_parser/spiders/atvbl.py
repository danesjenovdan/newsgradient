from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime


class AtvblSpider(CustomSpider):

    name = 'atvbl'

    allowed_domains = ['atvbl.rs']
    start_urls = ['https://www.atvbl.rs/']

    medium_id = 1

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'div.headline-news > a',
        'a.d-block'
    ]

    # ARTICLE PAGE
    news_title_class = 'h1.article-header-title::text'
    news_content_class = 'div.article-content>p ::text'
    ignore_starts_words = []
    skip_after = ''
    date_element = 'div.article-header li>span::text'

    def parse_news(self, response):
        # skip promo urls
        if '/atv/program/' in response.url:
            return
        return super().parse_news(response)

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return
        if len(date_strings[0].split('.')) == 4:
            date = ' '.join(date_strings[0:2])
        else:
            date = ' '.join(date_strings[1:3])
        formated_date = datetime.strptime(date, '%d.%m.%Y. %H:%M')
        return formated_date
