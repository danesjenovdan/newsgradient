# Generated by Django 3.0.6 on 2021-09-06 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20210904_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='uri',
            field=models.TextField(primary_key=True, serialize=False),
        ),
    ]
