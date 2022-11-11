from itertools import count
from analize.models import Media, News

from django.core.management.base import BaseCommand
from urllib.parse import urlparse
from datetime import datetime

import csv

# csv files we are going to parse
csvfiles = [
  'Historical-Report-NewsGradient-2022-09-02--2022-09-09.csv',
  'Historical-Report-NewsGradient-2022-09-09--2022-09-12.csv',
  'Historical-Report-NewsGradient-2022-09-12--2022-09-13.csv',
  'Historical-Report-NewsGradient-2022-09-13--2022-09-14.csv',
  'Historical-Report-NewsGradient-2022-09-14--2022-09-15.csv',
  'Historical-Report-NewsGradient-2022-09-15--2022-09-16.csv',
  'Historical-Report-NewsGradient-2022-09-16--2022-09-17.csv',
  'Historical-Report-NewsGradient-2022-09-17--2022-09-18.csv',
  'Historical-Report-NewsGradient-2022-09-18--2022-09-19.csv',
  'Historical-Report-NewsGradient-2022-09-19--2022-09-20.csv',
  'Historical-Report-NewsGradient-2022-09-20--2022-09-21.csv',
  'Historical-Report-NewsGradient-2022-09-21--2022-09-22.csv',
  'Historical-Report-NewsGradient-2022-09-22--2022-09-23.csv',
  'Historical-Report-NewsGradient-2022-09-23--2022-09-24.csv',
  'Historical-Report-NewsGradient-2022-09-24--2022-09-25.csv',
  'Historical-Report-NewsGradient-2022-09-25--2022-09-26.csv',
  'Historical-Report-NewsGradient-2022-09-26--2022-09-27.csv',
  'Historical-Report-NewsGradient-2022-09-27--2022-09-28.csv',
  'Historical-Report-NewsGradient-2022-09-28--2022-09-29.csv',
  'Historical-Report-NewsGradient-2022-09-29--2022-09-30.csv',
  'Historical-Report-NewsGradient-2022-09-30--2022-10-01.csv',
  'Historical-Report-NewsGradient-2022-10-01--2022-10-02.csv',
  'Historical-Report-NewsGradient-2022-10-02--2022-10-03.csv',
]

def domain_shortener(domain):
  d = urlparse(domain).netloc
  if d:
    return '.'.join(d.split('.')[-2:])
  else:
    return domain


class Command(BaseCommand):
    help = 'Parses css files with links to news articles in order to sort them by media and save them into separate css files.'

    def handle(self, *args, **options):
        for csv_file in csvfiles:
          filename = f"csv/{csv_file}"

          # get shortened domains for media in order to match spider names later
          media_names = {domain_shortener(x.link):x.name for x in Media.objects.all()}
          media_names['skipped'] = 'skipped'
          media = {domain_shortener(x.link):[] for x in Media.objects.all()}
          media['skipped'] = []

          with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)

            # skip headers
            next(reader)

            counter = 1
            counter_already_existing = 0
            counter_facebook_link = 0
            counter_saved = 0

            for row in reader:
              # post_created_date = row[10]
              news_link = row[31]
              
              # parse only n
              # if counter > 1:
              #   break

              try:
                # this news article is already in the database? -> skip
                News.objects.get(link=news_link)
                counter_already_existing += 1
                # print("Ze v bazi - SKIPPING")
              except:
                # this news article is not in the database
                domain = domain_shortener(news_link)
                # if link is facebook -> skip
                if "facebook" not in domain:
                  # append to correct media csv or to skipped
                  try:
                    media[domain].append([news_link, filename, counter])
                    counter_saved += 1
                  except:
                    media['skipped'].append([news_link, filename, counter])
                    counter_saved += 1
                else:
                  counter_facebook_link += 1
              
              counter += 1
              if counter % 100 == 0:
                print(filename, counter)

          print("NEWS THAT ALREADY EXIST IN THE DATABASE: ", counter_already_existing)
          print("FACEBOOK LINKS: ", counter_facebook_link)
          print("LINKS WE SAVED: ", counter_saved)
          print("NEWS PROCESSED: ", counter-1)
          print(f"MATCHING CHECK: {counter_already_existing + counter_facebook_link + counter_saved} == {counter-1} ?")
          
          # write to file
          for medium, link_list in media.items():
            with open(f'generated_csv/{media_names[medium]}.csv', 'a', newline='') as csvfile:
              w = csv.writer(csvfile)
              for l in link_list:
                w.writerow(l)
