# Generated by Django 3.2.4 on 2022-10-26 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analize', '0006_auto_20220920_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='parser_names',
            field=models.TextField(verbose_name='Parser names separated with |'),
        ),
    ]