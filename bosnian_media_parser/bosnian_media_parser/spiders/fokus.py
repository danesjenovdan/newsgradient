from bosnian_media_parser.spiders.spider import CustomSpider
from datetime import datetime
class N1infoSpider(CustomSpider):

    name = 'fokus'
    allowed_domains = ['fokus.ba']
    start_urls = ['https://www.fokus.ba/']

    medium_id = 1

    # HOMEPAGE
    allowed_home_page_div_classes = [
        '#home-mid-wrap a[rel="bookmark"]',
        'div.feat-widget-in.left.relative a'
    ]

    # ARTICLE PAGE
    news_title_class = 'h1.post-title::text'
    news_content_class = 'div#content-main>p ::text'
    ignore_starts_words = ['— @fokus', 'googletag.cmd.push', '(adsbygoogle']
    skip_after = 'Vaša email adresa neće biti objavljivana.'
    date_element = 'meta[property="article:published_time"]::attr(content)'

    #2022-08-23T10:50:25+02:00
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
