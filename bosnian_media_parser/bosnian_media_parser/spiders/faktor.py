from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime

class N1infoSpider(CustomSpider):

    name = 'faktor'

    allowed_domains = ['faktor.ba']
    start_urls = ['https://faktor.ba/']

    medium_id = 1

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'div.small-news > a',
        'div.main-news-big > a',
        'div.smallest-news > a',
        'div.big-news > a',
        'div.magazin-news-big after > a',
        'div.interesting-news-big after > a',
        'div.tehnomag-news-big > a',
        'div.video-big-news > a',
        'div.video-small-news > a',
        'div.economy-news-small > a',
        'div.economy-news-big > a',
    ]

    # ARTICLE PAGE
    news_title_class = 'h1.big-title::text'
    news_content_class = 'div.post-content > p::text'
    ignore_starts_words = []
    skip_after = ''
    date_element = 'p.time-meta::text'

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return
        date = date_strings[0].strip()
        formated_date = datetime.strptime(date, '%d.%m.%Y. / %H:%M')
        return formated_date



