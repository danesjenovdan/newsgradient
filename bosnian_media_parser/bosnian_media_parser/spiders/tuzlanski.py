from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime

class TuzlanskiSpider(CustomSpider):

    name = 'tuzlanski'

    allowed_domains = ['tuzlanski.ba']
    start_urls = ['https://tuzlanski.ba/']

    medium_id = 1

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'div.carsija-post-naslovnica > a',
        'div.drugi-blok-izdvojeno > div > a',
        'div.prvi-blok-izdvojeno > a',
        'div.post > a',
        'div.hronika-post-naslovnica > a',
        'div.maksuzija-post-naslovnica > a',
        'div.fotka-tab-lijevo > a'
    ]

    # ARTICLE PAGE
    news_title_class = 'article > h1.articleHeadline::text'
    news_content_class = 'div.article-content > p ::text'
    ignore_starts_words = []
    skip_after = 'Tuzlanski.ba možete pratiti i putem aplikacija za'
    date_element = 'time.article-date::text'

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return
        date = date_strings[1].strip()
        formated_date = datetime.strptime(date, '%d.%m.%Y. u %H:%M')
        return formated_date



