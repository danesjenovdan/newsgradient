from django.db import models
from martor.models import MartorField


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField(db_index=True)
    text = MartorField()
