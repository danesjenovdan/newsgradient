from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime


class JabukaSpider(CustomSpider):

    name = 'jabuka'

    allowed_domains = ['jabuka.tv']
    start_urls = ['https://www.jabuka.tv/']

    medium_id = 23

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'div.vce-grid-text>a',
        'div.meta-image>a'
    ]

    # ARTICLE PAGE
    news_title_class = 'h1.entry-title::text'
    news_content_class = 'div.entry-content>p ::text'
    ignore_starts_words = []
    skip_after = ''
    date_element = 'div.date>span.updated::text'

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma

        months = {
            'siječanja': '1',
            'veljača': '2',
            'ojužaka': '3',
            'travanja': '4',
            'svibanja': '5',
            'lipanja': '6',
            'srpanja': '7',
            'kolovoza': '8',
            'rujna': '9',
            'listopada': '10',
            'studena': '11',
            'prosinca': '12',
        }

        if not date_strings:
            return
        date_str = date_strings[0].strip().split(' ')
        print(date_str)
        date_str[1] = months[date_str[1]]
        date = ' '.join(date_str)
        formated_date = datetime.strptime(date, '%d. %m %Y.')
        return formated_date
