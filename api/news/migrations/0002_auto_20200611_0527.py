# Generated by Django 3.0.6 on 2020-06-11 05:27

from django.db import migrations
from django.db import models

import constants


class Migration(migrations.Migration):
    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-article_count']},
        ),
        migrations.AddField(
            model_name='medium',
            name='reliability',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='medium',
            name='slant',
            field=models.PositiveSmallIntegerField(
                blank=True,
                choices=[(constants.Orientations['LEFT'], 'Far left'),
                         (constants.Orientations['NEUTRAL'], 'Neutral'),
                         (constants.Orientations['RIGHT'], 'RIGHT')],
                null=True),
        ),
    ]
