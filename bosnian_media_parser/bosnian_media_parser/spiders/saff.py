from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime

class SaffSpider(CustomSpider):

    name = 'saff'

    allowed_domains = ['saff.ba']
    start_urls = ['https://saff.ba/']

    medium_id = 1

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'div.elementor-widget-container>span>a',
    ]

    # ARTICLE PAGE
    news_title_class = 'h1.elementor-heading-title::text'
    news_content_class = 'div.elementor-widget-theme-post-content>div.elementor-widget-container>p ::text'
    ignore_starts_words = []
    skip_after = ''
    date_element = 'meta[itemprop="datePublished"]::attr(content)'

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return
        date = date_strings[0].strip()
        formated_date = datetime.strptime(date, '%Y-%m-%d')
        return formated_date



