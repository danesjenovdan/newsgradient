from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime

import re

class RtrsSpider(CustomSpider):

    name = 'rtrs'

    allowed_domains = ['rtrs.tv']
    start_urls = ['https://www.rtrs.tv/']

    medium_id = 36

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'article > a',
        'ul.ul-najnovije > li > a',
    ]

    # ARTICLE PAGE
    news_title_class = 'h1.naslov_vijesti::text'
    news_content_class = 'div.nwzbody>p::text'
    ignore_starts_words = []
    skip_after = ''
    date_element = 'div.vrijeme-izvor::text'

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        find_date = "^\d{2}\/\d{2}\/\d{4} \|  \d{2}:\d{2}"
        # preskoči page če nima datuma
        if not date_strings:
            return
        date = date_strings[0].strip().replace(u'\xa0', u' ').split("⇒ ")[0].strip()
        date = re.findall(find_date, date)
        formated_date = datetime.strptime(date[0], '%d/%m/%Y |  %H:%M')
        return formated_date
