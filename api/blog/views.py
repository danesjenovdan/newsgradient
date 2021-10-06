from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from . import serializers
from .models import BlogPost


class BlogPostViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BlogPostSerializer
    queryset = BlogPost.objects.all()
    permission_classes = (AllowAny,)


class BlogPostView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, blogpost_id):
        blogpost = BlogPost.objects.get(blogpost_id)
        bp_serializer = serializers.BlogPostSerializer
        data = bp_serializer.dump(blogpost)
        return Response(data)
