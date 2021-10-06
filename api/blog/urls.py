from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'', views.BlogPostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('/<str:blogpost_id>/', views.BlogPostView.as_view()),
]
