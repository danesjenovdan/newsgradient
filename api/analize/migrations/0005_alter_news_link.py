# Generated by Django 3.2.4 on 2022-09-01 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analize', '0004_auto_20220901_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='link',
            field=models.URLField(blank=True, max_length=512, null=True, verbose_name='News link'),
        ),
    ]
