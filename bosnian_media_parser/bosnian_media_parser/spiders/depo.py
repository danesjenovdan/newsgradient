from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime


class DepoSpider(CustomSpider):

    name = 'depo'

    allowed_domains = ['depo.ba']
    start_urls = ['https://depo.ba/']

    medium_id = 13

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'ul.slides > li > a',
        'div.media > a',
        'a.media',
        'div.sliderBlockArticle > a'
    ]

    # ARTICLE PAGE
    news_title_class = 'h1.mainHeader::text'
    news_content_class = 'div.articleContent>p ::text'
    ignore_starts_words = []
    skip_after = ''
    date_element = 'p.writtenBy::text'

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return
        date = date_strings[0].strip()

        formated_date = datetime.strptime(date, '%d.%m.%y, %H:%Mh')
        return formated_date
