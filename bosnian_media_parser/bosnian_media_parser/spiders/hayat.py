from bosnian_media_parser.spiders.spider import CustomSpider
from datetime import datetime
class N1infoSpider(CustomSpider):

    name = 'hayat'
    allowed_domains = ['hayat.ba']
    start_urls = ['https://hayat.ba/']

    medium_id = 1

    # HOMEPAGE
    allowed_home_page_div_classes = ['div.td-main-content-wrap div.wpb_row>div.tdc-column>div.wpb_wrapper div.td-module-thumb>a']

    # ARTICLE PAGE
    news_title_class = 'h1.tdb-title-text::text'
    news_content_class = 'div.td-post-content ::text'
    ignore_starts_words = ['/* custom css', 'googletag.cmd.push', '(adsbygoogle']
    skip_after = None
    date_element = 'time.entry-date::attr(datetime)'

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
