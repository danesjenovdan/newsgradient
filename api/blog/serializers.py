from rest_framework import serializers
import markdown
from . import models


class BlogPostSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['text'] = markdown.markdown(ret['text'])
        return ret

    class Meta:
        model = models.BlogPost
        fields = ['id', 'short_description', 'image', 'title', 'date', 'text']
