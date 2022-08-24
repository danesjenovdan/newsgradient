from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime

class N1infoSpider(CustomSpider):

    name = 'vijesti'

    allowed_domains = ['vijesti.ba']
    start_urls = ['https://vijesti.ba/']

    medium_id = 1

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'div.featured-imgs > a',
        'div.mm-large-text > a',
        'div.mm-small-text > a',
        'div.side-article-title > a',
        'div.posed > a',
        'div.featured-item__thumb > a'
    ]

    # ARTICLE PAGE
    news_title_class = 'h1.single-title::text'
    news_content_class = 'div.single-text ::text'
    ignore_starts_words = []
    skip_after = 'Pratite nas na'
    date_element = 'h4.single-suptitle::text'

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return
        date = ' '.join(date_strings[0].replace('/','').replace('  ', ' ').split(' ')[:2])
        formated_date = datetime.strptime(date, '%d.%m.%Y %H:%M')
        return formated_date



