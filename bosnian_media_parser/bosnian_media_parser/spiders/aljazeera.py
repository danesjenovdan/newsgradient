from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime

class AljazeeraSpider(CustomSpider):

    name = 'aljazeera'
    allowed_domains = ['aljazeera.net', 'ajb.me']
    start_urls = ['https://balkans.aljazeera.net/', 'https://ajb.me/']

    medium_id = 1

    # HOMEPAGE
    allowed_home_page_div_classes = [
        '.container.container--white.container--no-mobile-padding a',
        '#news-feed-container a'
    ]

    # ARTICLE PAGE
    news_title_class = '.article-header h1::text'
    news_content_class = 'div.wysiwyg--all-content ::text'
    ignore_starts_words = []
    skip_after = None
    date_element = 'div.date-simple ::text'

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return
        date = date_strings[1]
        formated_date = datetime.strptime(date, '%d %b %Y')
        return formated_date
