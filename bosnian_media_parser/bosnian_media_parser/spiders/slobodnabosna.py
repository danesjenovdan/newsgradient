from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime


class N1infoSpider(CustomSpider):

    name = 'slobodna-bosna'

    allowed_domains = ['slobodna-bosna.ba']
    start_urls = ['https://www.slobodna-bosna.ba/']

    medium_id = 1

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'article > a',
    ]

    # ARTICLE PAGE
    news_title_class = 'header > h1::text'
    news_content_class = 'div.tinymce>p::text'
    ignore_starts_words = []
    skip_after = ''
    date_element = ''

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return
        # date = date_strings[0].strip()

        # formated_date = datetime.strptime(date, '%d.%m.%y, %H:%Mh')
        return None
