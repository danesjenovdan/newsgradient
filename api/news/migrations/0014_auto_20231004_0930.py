# Generated by Django 3.2.4 on 2023-10-04 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_auto_20211103_0959'),
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Name')),
                ('parser_names', models.TextField(verbose_name='Parser names separated with |')),
            ],
        ),
        migrations.CreateModel(
            name='PartyMediumScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(blank=True, decimal_places=7, max_digits=10, null=True, verbose_name='Score')),
                ('neutral_score', models.DecimalField(blank=True, decimal_places=7, max_digits=10, null=True, verbose_name='Neutral score')),
                ('medium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partymediumscore', to='news.medium', verbose_name='Medium')),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partymediumscore', to='news.party', verbose_name='Party')),
            ],
        ),
        migrations.AddField(
            model_name='party',
            name='mediumscore',
            field=models.ManyToManyField(related_name='parties', through='news.PartyMediumScore', to='news.Medium', verbose_name='Medium score'),
        ),
        migrations.AddField(
            model_name='medium',
            name='partyscore',
            field=models.ManyToManyField(related_name='medias', through='news.PartyMediumScore', to='news.Party', verbose_name='Party score'),
        ),
    ]
