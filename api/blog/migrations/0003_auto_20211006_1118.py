# Generated by Django 3.2.4 on 2021-10-06 11:18

from django.db import migrations, models
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField(db_index=True)),
                ('text', martor.models.MartorField()),
            ],
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]