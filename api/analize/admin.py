from django.contrib import admin
from analize.models import News, Media, Party, Member

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
        'location'
    ]


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


admin.site.register(News, NewsAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Party, PartyAdmin)
admin.site.register(Member, MemberAdmin)
