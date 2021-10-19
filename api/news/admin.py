from django.contrib import admin, messages
from django.db.models import Count, IntegerField, Q, ManyToManyField
from django.db.models.functions import Cast
from django.template.response import TemplateResponse
from django.utils.translation import ngettext
from django.utils.safestring import mark_safe
from django import forms

from datetime import datetime, timedelta

from constants import Orientations
from news import models

# Register your models here.

class MediumAdmin(admin.ModelAdmin):
    list_display = ['title', 'uri', 'slant', 'favicon']
    search_fields = ['title', 'uri']
    list_filter = ['slant']
    list_editable = ('slant',)


class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'number_of_articles', 'is_promoted', 'left_count', 'neutral_count', 'right_count']
    search_fields = ['title', 'summary']
    list_filter = ['date', 'is_promoted']
    list_editable = ('is_promoted',)
    exclude = ['uri', 'images']

    def get_queryset(self, request):
        return models.Event.objects.prefetch_related('articles').all().annotate(
            _all_count=Cast(
                Count(
                    'articles',
                    filter=Q(articles__medium__slant__isnull=False),
                    distinct=True
                ),
                IntegerField()
            ),
            _left_count=Cast(
                Count(
                    'articles',
                    filter=Q(articles__medium__slant=Orientations.LEFT.value),
                    distinct=True
                ),
                IntegerField()
            ),
            _neutral_count=Cast(
                Count(
                    'articles',
                    filter=Q(articles__medium__slant=Orientations.NEUTRAL.value),
                    distinct=True
                ),
                IntegerField()
            ),
            _right_count=Cast(
                Count(
                    'articles',
                    filter=Q(articles__medium__slant=Orientations.RIGHT.value),
                    distinct=True
                ),
                IntegerField()
            )
        )

    def number_of_articles(self, obj):
        return obj._all_count

    def left_count(self, obj):
        return obj._left_count

    def neutral_count(self, obj):
        return obj._neutral_count

    def right_count(self, obj):
        return obj._right_count

    def merge_to_oldest(self, request, queryset):
        first_event = queryset.earliest('date')
        other_events = queryset.exclude(uri=first_event.uri)

        if request.POST.get('post'):
            for event in other_events:
                event.articles.all().update(event=first_event)
            other_events.delete()
            self.message_user(request, 'Articles was successfully added to event: %s' %first_event.title , messages.SUCCESS)
        else:
            request.current_app = self.admin_site.name
            lala = {
                'queryset': queryset,
                'action': 'merge_to_oldest',
                'parent_event': first_event,
                'other_events': other_events,
                'c_action': 'move articles of events to oldest event and delete newest events.',
            }
            return TemplateResponse(request, "admin/action_confirmation.html", context=lala)

    def merge_to_most_popular(self, request, queryset):
        print(queryset)
        sorted_events = queryset.annotate(ac=Count('articles')).order_by('-ac')
        first_event = sorted_events[0]
        other_events = sorted_events.exclude(uri=first_event.uri)
        if request.POST.get('post'):
            for event in other_events:
                event.articles.all().update(event=first_event)
            other_events.delete()
            self.message_user(request, 'Articles was successfully added to event: %s' %first_event.title , messages.SUCCESS)
        else:
            request.current_app = self.admin_site.name
            lala = {
                'queryset': queryset,
                'parent_event': first_event,
                'action': 'merge_to_most_popular',
                'other_events': other_events,
                'c_action': 'move articles of events to the most popular event and delete other events.'
            }
            return TemplateResponse(request, "admin/action_confirmation.html", context=lala)

    def save_model(self, request, obj, form, change):
        # check if is_promoted was turned on
        # and if it was, add the event to the newsletter
        if (
            'is_promoted' in form.initial.keys()
        ) and (
            form.initial.get('is_promoted', None) == False
        ) and (
            change == True
        ):
            newsletter = models.Newsletter.objects.filter(
                sent=False
            ).order_by(
                '-date'
            ).first()
            # if there is no valid newsletter raise a ValueError
            if not newsletter:
                raise ValueError('YOU NEED TO SET UP A NEWSLETTER MOFO!')

            #  add events to the newsletter
            newsletter.events.add(obj)
        super().save_model(request, obj, form, change)

    actions = [merge_to_oldest, merge_to_most_popular]

    number_of_articles.admin_order_field = '_all_count'
    left_count.admin_order_field = '_left_count'
    neutral_count.admin_order_field = '_neutral_count'
    right_count.admin_order_field = '_right_count'


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'event', 'medium']
    search_fields = ['title', 'content']
    list_filter = ['event', 'medium']
    list_select_related = ('medium',)
    autocomplete_fields = ['event']


class NewsletterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['events'].queryset = models.Newsletter.objects.get(
            id=kwargs['instance'].id
        ).events.all()


class NewsletterAdmin(admin.ModelAdmin):
    form = NewsletterForm
    formfield_overrides = {
        ManyToManyField: {'widget': forms.CheckboxSelectMultiple(attrs={'style': 'margin-right: 10px'})},
    }

admin.site.register(models.Medium, MediumAdmin)
admin.site.register(models.Event, EventAdmin)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Tweet)
admin.site.register(models.Newsletter, NewsletterAdmin)
