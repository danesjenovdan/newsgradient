from django.contrib import admin
from analize.models import News, Media, Party, Member, PartyMediaScore

from datetime import datetime, timedelta

# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'link',
        'published_at',
        'media'
    ]
    list_filter = ['media']


class MediaAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'link',
        'location',
        'news_count',
        'news_count_last_day',
    ]

    def news_count(self, obj):
        return obj.news.count()

    def news_count_last_day(self, obj):
        return obj.news.filter(parsed_at__gte=datetime.now()-timedelta(days=1)).count()


class PartyAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'parser_names'
    ]


class MemberAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'parser_names'
    ]


class PartyMediaScoreAdmin(admin.ModelAdmin):
    list_display = [
        'party',
        'media',
        'score',
        'neutral_score'
    ]
    list_filter = ['party', 'media']
    list_editable = ['score', 'neutral_score']


admin.site.register(News, NewsAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Party, PartyAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(PartyMediaScore, PartyMediaScoreAdmin)
