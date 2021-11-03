from django.db import models
from martor.models import MartorField


class BlogPost(models.Model):
    title = models.TextField()
    short_description = models.TextField()
    date = models.DateField(db_index=True)
    image = models.ImageField(
        upload_to='media/blog-images',
        null=True,
        blank=True
    )
    text = MartorField()

    def __str__(self):
        return self.title
