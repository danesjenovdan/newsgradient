# Generated by Django 3.2.4 on 2021-10-06 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(default='title', max_length=255),
            preserve_default=False,
        ),
    ]
