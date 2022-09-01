from django.contrib import admin
from analize.models import News, Media

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


admin.site.register(News, NewsAdmin)
admin.site.register(Media, MediaAdmin)
