from django.core.management import BaseCommand

from news.models import Medium


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Please enter the path to the csv file.')
        file_path = input()
        with open(file_path, 'r') as infile:
            for i, line in enumerate(infile.readlines()):
                if i > 0:
                    title, uri, favicon, slant, is_embeddable, reliability = line.split(',')

                    existing_medium = Medium.objects.filter(uri=uri).first()
                    if not existing_medium:
                        Medium.objects.create(
                            title=title,
                            uri=uri,
                            favicon=favicon,
                            slant=slant,
                            is_embeddable=is_embeddable,
                            reliability=reliability
                        )
