from bosnian_media_parser.spiders.spider import CustomSpider

from datetime import datetime
import scrapy
import re


class BhrtSpider(CustomSpider):

    name = 'bhrt'

    allowed_domains = ['bhrt.ba']
    start_urls = ['https://bhrt.ba/api/?lng=null']

    medium_id = 6


    def parse(self, response):
        data = response.json()
        for key, category in data.items():
            print(category)
            if category == 'LAT' or not 'data' in category.keys():
                continue
            if not isinstance(category['data'], list):
                continue
            for item in category['data']:
                print("ITEM", type(item))
                print(item)
                if 'url' in item.keys():
                    yield scrapy.Request(
                        url=f'https://bhrt.ba/api/{item["url"]}',
                        callback=self.parse_item
                    )

    def parse_item(self, response):
        to_clean = re.compile('<.*?>')
        data = response.json()[0]
        print(data['DTPublished'])
        formated_date = datetime.strptime(data['DTPublished'].split('.')[0], '%Y-%m-%dT%H:%M:%S')
        cleantext = re.sub(to_clean, '', data['Content'])
        yield {
            'title': data['Title'],
            'content': cleantext,
            'array': [cleantext],
            'medium_id': self.medium_id,
            'url': response.url,
            'date': formated_date,
        }




