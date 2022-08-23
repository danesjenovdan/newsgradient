from bosnian_media_parser.spiders.spider import CustomSpider
from datetime import datetime
class N1infoSpider(CustomSpider):

    name = 'buka'
    allowed_domains = ['6yka.com']
    start_urls = ['https://6yka.com/']

    medium_id = 1

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'div.standard-article-card-wrapper>a'
    ]

    # ARTICLE PAGE
    news_title_class = 'h1.title::text'
    news_content_class = 'div.article-content ::text'
    ignore_starts_words = []
    skip_after = ''
    date_element = '.article-time::text'

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return
        print(date_strings)
        date = date_strings[0].strip()

        formated_date = datetime.strptime(date, '%d. %B %Y, %H:%M')
        return formated_date
