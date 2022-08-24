import scrapy
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, "bs_BA.UTF-8")

class CustomSpider(scrapy.Spider):

  # spider settings
  name = 'scraper_name'
  allowed_domains = ['example.com']
  start_urls = ['https://example.com/']

  # medium data settings
  medium_id = 1

  # HOMEPAGE
  # a list of css classes we use to select which DOM elements to parse
  allowed_home_page_div_classes = ['div.class1', 'div.class2']

  # ARTICLE PAGE
  # css selector used to find the DOM element containing article title
  news_title_class = 'selector-example h1'
  # css selector used to find the DOM elements containing article contents
  news_content_class = 'selector-example .content'
  # array of strings that mark DOM elements which we should skip while collecting content
  ignore_starts_words = ['Izvor:', 'Podijeli:', 'iPhone/iPad']
  # skip the content found after this string
  skip_after = 'Program N1 televizije možete pratiti UŽIVO'
  # css selector used to find the date
  date_element = 'selector-example .post-time'


  def parse(self, response):
    """ Parses the medium home page and calls function parse_news on all found links to articles. """

    # sparsaj vse linke iz specifičnih div-ov iz home page-a
    for cls in self.allowed_home_page_div_classes:
        home_links = response.css(f'{cls}')
        yield from response.follow_all(home_links, self.parse_news)


  def parse_news(self, response):
    """ Parses the article page and yields the data. """

    # pridobi naslov in vsebino novice
    title = response.css(f'{self.news_title_class}').get().strip()
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
    """
    Parses string date format '%d. %b %Y %H:%M' to datetime.
    """

    date = ' '.join(date_strings).replace('>', '').strip()

    # če je mesec avgust se zamenja ime meseca ker je v localah napačno ime meseca
    date = date.replace('avg', 'aug')

    # preskoči page če nima datuma
    if not date:
        return

    formated_date = datetime.strptime(date, '%d. %b %Y %H:%M')
    return formated_date


  def skip_items_and_merge(self, texts):
    """ 
    Parse article contents and merge them into a single string. 
    Skip those elements that start with any of ignore_starts_words strings.
    Skip all content after skip_after string.
    """
    
    for i, text in enumerate(texts):
        for word in self.ignore_starts_words:
            if text.strip().startswith(word):
                texts[i] = ''

    content = ' '.join(map(str.strip, texts))

    if self.skip_after and self.skip_after in content:
        content = content[:content.index(self.skip_after)]
    return content
