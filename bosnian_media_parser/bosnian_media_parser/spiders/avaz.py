from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime

class N1infoSpider(CustomSpider):

    name = 'avaz'
    # ON HOLD

    # allowed_domains = ['avaz.ba']
    # start_urls = ['https://avaz.ba/']

    # medium_id = 1

    # # HOMEPAGE
    # allowed_home_page_div_classes = [
    #     'div.top-article-box',
    #     '#news-feed-container'
    # ]

    # # ARTICLE PAGE
    # news_title_class = '.article-header h1::text'
    # news_content_class = 'div.wysiwyg--all-content ::text'
    # ignore_starts_words = []
    # skip_after = None
    # date_element = 'div.date-simple ::text'

    # def parse_date(self, date_strings):
    #     """
    #     Parses string date format '%d. %b %Y %H:%M' to datetime.
    #     """
    #     # preskoči page če nima datuma
    #     if not date_strings:
    #         return
    #     date = date_strings[1]
    #     formated_date = datetime.strptime(date, '%d %b %Y')
    #     return formated_date



