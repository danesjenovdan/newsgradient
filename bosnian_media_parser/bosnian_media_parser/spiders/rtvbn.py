from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime

class N1infoSpider(CustomSpider):

    name = 'rtvbn'

    allowed_domains = ['rtvbn.com']
    start_urls = ['https://www.rtvbn.com/']

    medium_id = 1

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'article.news-article > a',
        'div.recent-news>div.container>div.row a'
    ]

    # ARTICLE PAGE
    news_title_class = 'h1.title::text'
    news_content_class = 'article>div>p.txt ::text'
    ignore_starts_words = []
    skip_after = None
    date_element = 'article>div>span.date::text'

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return
        date = ''.join(date_strings[0].split('|')[:2]).strip()
        formated_date = datetime.strptime(date, '%d.%m.%Y  %H:%M')
        return formated_date



