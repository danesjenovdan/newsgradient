# Generated by Django 3.2.4 on 2023-10-04 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analize', '0008_partymediascore'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='partyscore',
            field=models.ManyToManyField(related_name='medias', through='analize.PartyMediaScore', to='analize.Party', verbose_name='Party score'),
        ),
        migrations.AddField(
            model_name='party',
            name='mediascore',
            field=models.ManyToManyField(related_name='parties', through='analize.PartyMediaScore', to='analize.Media', verbose_name='Media score'),
        ),
    ]
