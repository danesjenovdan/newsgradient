import scrapy
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, "bs_BA.UTF-8")

class N1infoSpider(scrapy.Spider):
    name = 'n1info'
    allowed_domains = ['n1info.com']
    start_urls = ['https://ba.n1info.com/']

    allowed_home_page_div_classes = ['featured-zone-homepage', 'content-zone']
    news_title_class = 'h1.entry-title::text'
    news_content_class = '.entry-content ::text'
    ignore_starts_words = ['Izvor:', 'Podijeli:', 'iPhone/iPad']

    date_element = '.post-time span::text'

    skip_after = 'Program N1 televizije možete pratiti UŽIVO'
    medium_id = 1

    def parse(self, response):
        # sparsaj vse linke iz specifičnih div-ov iz home page-a
        for cls in self.allowed_home_page_div_classes:
            home_links = response.css(f'div.{cls} a')
            yield from response.follow_all(home_links, self.parse_news)

    def parse_news(self, response):
        # pridobi naslov in vsebino novice
        title = response.css(f'{self.news_title_class}').get()
        content_list = response.css(f'{self.news_content_class}').getall()

        # prečišči besedilo
        cleard_content = self.skip_items_and_merge(content_list)

        # parsanje datuma
        date_strings = response.css(f'{self.date_element}').getall()

        formated_date = self.parse_date(date_strings)

        yield {
            'title': title,
            'content': cleard_content.strip(),
            'array': content_list,
            'medium_id': self.medium_id,
            'url': response.url,
            'date': formated_date,
        }

    def parse_date(self, date_strings):
        date = ' '.join(date_strings).replace('>', '').strip()

        # če je mesec avgust se zamenja ime meseca ker je v localah napačno ime meseca
        date = date.replace('avg', 'aug')

        # preskoči page če nima datuma
        if not date:
            return

        formated_date = datetime.strptime(date, '%d. %b %Y %H:%M')
        return formated_date

    def skip_items_and_merge(self, texts):
        for i, text in enumerate(texts):
            for word in self.ignore_starts_words:
                if text.strip().startswith(word):
                    texts[i] = ''

        content = ' '.join(map(str.strip, texts))
        if self.skip_after in content:
            content = content[:content.index(self.skip_after)]
        return content
