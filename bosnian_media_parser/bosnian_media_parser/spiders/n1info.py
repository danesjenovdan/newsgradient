from bosnian_media_parser.spiders.spider import CustomSpider

class N1infoSpider(CustomSpider):

    name = 'n1info'
    allowed_domains = ['n1info.com']
    start_urls = ['https://ba.n1info.com/']

    medium_id = 1

    # HOMEPAGE
    allowed_home_page_div_classes = ['featured-zone-homepage', 'content-zone']
    
    # ARTICLE PAGE
    news_title_class = 'h1.entry-title::text'
    news_content_class = '.entry-content ::text'
    ignore_starts_words = ['Izvor:', 'Podijeli:', 'iPhone/iPad']
    skip_after = 'Program N1 televizije možete pratiti UŽIVO'
    date_element = '.post-time span::text'
