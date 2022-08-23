from bosnian_media_parser.spiders.spider import CustomSpider
from datetime import datetime
class N1infoSpider(CustomSpider):

    name = 'face'
    allowed_domains = ['face.ba']
    start_urls = ['https://www.face.ba/']

    medium_id = 1

    # HOMEPAGE
    allowed_home_page_div_classes = [
        '.article > a'
    ]

    # ARTICLE PAGE
    news_title_class = 'div.main-article-headline::text'
    news_content_class = 'div.main-article-text-wrapper ::text'
    ignore_starts_words = ['var mpi_wi']
    skip_after = ''
    date_element = '.main-article-info>span.main-article-info-span::text'

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return
        print(date_strings)
        date = date_strings[0].strip()

        formated_date = datetime.strptime(date, '%d. %m. %Y. u %H:%M')
        return formated_date
