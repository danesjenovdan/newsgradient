from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime


class VecernjiSpider(CustomSpider):

    name = 'novi'

    allowed_domains = ['novi.ba']
    start_urls = ['https://novi.ba/']

    medium_id = 50

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'a.pjax-article',
    ]

    # ARTICLE PAGE
    news_title_class = 'div.head_article>h1::text'
    news_content_class = 'div.content>p ::text'
    ignore_starts_words = []
    skip_after = ''
    date_element = 'div.date_published::text'

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return
        date = date_strings[0].strip()
        formated_date = datetime.strptime(date, '%d.%m.%Y - %H:%M')
        return formated_date
