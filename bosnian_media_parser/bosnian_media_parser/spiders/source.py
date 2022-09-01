from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime


class SourceSpider(CustomSpider):

    name = 'source'

    allowed_domains = ['source.ba']
    start_urls = ['https://source.ba/']

    medium_id = 40

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'a'

    ]

    # ARTICLE PAGE
    news_title_class = 'div.naslovTekstualnogClanka::text'
    news_content_class = 'div.tekstTekstualnogClanka>p ::text'
    ignore_starts_words = []
    skip_after = ''
    date_element = 'div.vrijemeObjaveClanka ::text'

    def parse_news(self, response):
        # parse just news links
        if '/clanak/' in response.url:
            return super().parse_news(response)

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return
        date = date_strings[0].strip()
        formated_date = datetime.strptime(date, '%d.%m.%Y. %H:%M')
        return formated_date



