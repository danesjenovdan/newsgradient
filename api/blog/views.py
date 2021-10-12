from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework import pagination

from . import serializers
from .models import BlogPost

import os
import json
import uuid

from django.conf import settings
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from martor.utils import LazyEncoder


@login_required
def markdown_uploader(request):
    """
    Makdown image upload for locale storage
    and represent as json to markdown editor.
    """
    if request.method == 'POST' and request.is_ajax():
        if 'markdown-image-upload' in request.FILES:
            image = request.FILES['markdown-image-upload']
            image_types = [
                'image/png', 'image/jpg',
                'image/jpeg', 'image/pjpeg', 'image/gif'
            ]
            if image.content_type not in image_types:
                data = json.dumps({
                    'status': 405,
                    'error': _('Bad image format.')
                }, cls=LazyEncoder)
                return HttpResponse(
                    data, content_type='application/json', status=405)

#             if image._size > settings.MAX_IMAGE_UPLOAD_SIZE:
#                 to_MB = settings.MAX_IMAGE_UPLOAD_SIZE / (1024 * 1024)
#                 data = json.dumps({
#                     'status': 405,
#                     'error': _('Maximum image file is %(size) MB.') % {'size': to_MB}
#                 }, cls=LazyEncoder)
#                 return HttpResponse(
#                     data, content_type='application/json', status=405)

            img_uuid = "{0}-{1}".format(uuid.uuid4().hex[:10], image.name.replace(' ', '-'))
            tmp_file = os.path.join(settings.MARTOR_UPLOAD_PATH, img_uuid)
            def_path = default_storage.save(tmp_file, ContentFile(image.read()))
            # S3 FILES MUST BE PUBLIC, OR IT WON'T WORK!
            if os.getenv('DJANGO_ENABLE_S3', False):
                img_url = settings.AWS_S3_ENDPOINT_URL + '/' + settings.AWS_STORAGE_BUCKET_NAME + '/' + settings.AWS_LOCATION + '/' + def_path
            else:
                img_url = settings.BASE_URL + settings.MEDIA_URL + def_path

            data = json.dumps({
                'status': 200,
                'link': img_url,
                'name': image.name
            })
            return HttpResponse(data, content_type='application/json')
        return HttpResponse(_('Invalid request!'))
    return HttpResponse(_('Invalid request!'))


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 9
    page_query_param = 'page'


class BlogPostViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BlogPostSerializer
    pagination_class = StandardResultsSetPagination
    queryset = BlogPost.objects.all().order_by('-date')
    permission_classes = (AllowAny,)


class BlogPostView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, blogpost_id):
        blogpost = BlogPost.objects.get(blogpost_id)
        bp_serializer = serializers.BlogPostSerializer
        data = bp_serializer.dump(blogpost)
        return Response(data)
