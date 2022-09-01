from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime


class GlassrpskeSpider(CustomSpider):

    name = 'glassrpske'

    allowed_domains = ['glassrpske.com']
    start_urls = ['http://glassrpske.com/']

    medium_id = 1

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'div.card > a',
        'a.lista-link'
    ]

    # ARTICLE PAGE
    news_title_class = 'h1.naslov-citava::text'
    news_content_class = 'section>p ::text'
    ignore_starts_words = []
    skip_after = 'Пратите нас на нашој'
    date_element = 'header time::attr(datetime)'

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return
        date = date_strings[0].split('+')[0]
        formated_date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
        return formated_date
