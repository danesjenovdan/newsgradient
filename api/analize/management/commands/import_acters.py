from analize.models import Member, Party

from django.core.management.base import BaseCommand
import xlrd

class Command(BaseCommand):
    help = 'Import parties'

    def handle(self, *args, **options):


        file_path='analize/files/ng_party_members.xlsx'
        book = xlrd.open_workbook(file_path)
        for sheet in book.sheets():
            party_names = []
            members = []
            for row_i in range(sheet.nrows):
                row = sheet.row(row_i)
                party_names.append(row[0].value)
                members.append(row[1].value)

            print(party_names)
            print(members)
            self.add_party(party_names[1:], members[1:])


    def add_party(self, party_names, members):
        parser_names = '|'.join([name for name in party_names if name])
        party = Party(
            name=party_names[0],
            parser_names=parser_names
        )
        party.save()
        for member in members:
            if member:
                Member(name=member, parser_names=member, in_party=party).save()


