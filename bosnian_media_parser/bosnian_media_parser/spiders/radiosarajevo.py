from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime

class RadiosarajevoSpider(CustomSpider):

    name = 'radiosarajevo'
    allowed_domains = ['radiosarajevo.ba']
    start_urls = ['https://radiosarajevo.ba/']

    medium_id = 33

    # HOMEPAGE
    allowed_home_page_div_classes = [
        'div.main>section article>a',
    ]

    # ARTICLE PAGE
    news_title_class = 'article>h1::text'
    news_content_class = 'article div.text-editor ::text'
    ignore_starts_words = ['_ipromNS']
    skip_after = None
    date_element = 'time.time::attr(datetime)'

    def parse_date(self, date_strings):
        """
        Parses string date format '%d. %b %Y %H:%M' to datetime.
        """
        # preskoči page če nima datuma
        if not date_strings:
            return
        date = date_strings[0]
        formated_date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        return formated_date



