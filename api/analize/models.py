from re import T
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Media(models.Model):
    class Locations(models.TextChoices):
        SARAJEVO = 'KS', _('Kanton Sarajevo')
        SRPSKA = 'RS', _('Republika Srpska')
        UNSOSANSKI = 'US', _('Unsko-Sanski kanton')
        HERCEGOVACKO = 'HN', _('Hercegovačko-neretvanski kanton')
        TUZLANSKI = 'TK', _('Tuzlanski kanton')
        ZENICKO = 'ZD', _('Zeničko-dobojski kanton')
        BRCKO = 'BD', _('Brčko distrikt')
    name = models.TextField(verbose_name=_('Name'))
    link = models.URLField(null=True, blank=True, verbose_name=_('Media\'s link'))
    location = models.CharField(
        max_length=2,
        choices=Locations.choices,
        default=Locations.SARAJEVO,
        verbose_name=_('Media\'s location')
    )
    fb_link = models.URLField(null=True, blank=True, verbose_name=_('Facebook link'))
    tw_link = models.URLField(null=True, blank=True, verbose_name=_('Twitter link'))

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.TextField(verbose_name=_('Name'))
    parser_names = models.TextField(verbose_name=_('Parser names divided with |'))

    def __str__(self):
        return self.name


class Party(Actor):
    pass


class Member(Actor):
    pass


class PartyNewsMention(models.Model):
    party = models.ForeignKey('Party', on_delete=models.CASCADE, related_name='parties_through', verbose_name=_('Party'))
    news = models.ForeignKey('News', on_delete=models.CASCADE, related_name='partynews_through', verbose_name=_('News'))
    score = models.IntegerField(null=True, blank=True, verbose_name=_('Score'))


class MembersNewsMention(models.Model):
    member = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='members_through', verbose_name=_('Member'))
    news = models.ForeignKey('News', on_delete=models.CASCADE, related_name='membernews_through', verbose_name=_('News'))
    score = models.IntegerField(null=True, blank=True, verbose_name=_('Score'))



class News(models.Model):
    title = models.TextField(verbose_name=_('Title'))
    content = models.TextField(verbose_name=_('Content'))
    link = models.URLField(null=True, blank=True, verbose_name=_('News link'), max_length=512)
    html = models.TextField(verbose_name=_('Html content'))
    media = models.ForeignKey('Media', on_delete=models.CASCADE, verbose_name=_('Media'), related_name='news')
    published_at = models.DateTimeField(null=True, blank=True, verbose_name=_('Published at'))
    parsed_at = models.DateTimeField(null=True, blank=True, verbose_name=_('Parsed at'))
    last_parsed_at = models.DateTimeField(null=True, blank=True, verbose_name=_('Last parsed at'))
    parties = models.ManyToManyField('Party', related_name='news', through='PartyNewsMention', verbose_name=_('Parties'))
    members = models.ManyToManyField('Member', related_name='news', through='MembersNewsMention', verbose_name=_('Members'))

    def __str__(self):
        return self.title

