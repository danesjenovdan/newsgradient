from bosnian_media_parser.spiders.spider import CustomSpider
from datetime import datetime
class NezavisneSpider(CustomSpider):

    name = 'nezavisne'
    allowed_domains = ['nezavisne.com']
    start_urls = ['https://www.nezavisne.com/']

    medium_id = 29

    # HOMEPAGE
    allowed_home_page_div_classes = [
        '.thumbnail > a',
        '.kutija-ljevo > a',
        '.media-popularno-ljevo > a'
    ]

    # ARTICLE PAGE
    news_title_class = 'header h1::text'
    news_content_class = 'div.vijestTijelo ::text'
    ignore_starts_words = ['googletag.cmd.push']
    skip_after = ''
    date_element = 'time.dateline::attr(datetime)'

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return

        date = date_strings[0].split('+')[0]
        formated_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")
        return formated_date
