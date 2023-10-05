from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from news import views

router = DefaultRouter()
router.register(r'events', views.EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('top-events/', views.TopEventsView.as_view()),
    path('top-filtered-events/', views.TopFilteredEventsView.as_view()),
    path('articles/<str:event_id>/', views.ArticleView.as_view()),
    path('event/<str:event_id>/', views.EventDetailView.as_view()),
    path('newsletter-preview/', views.NewsletterView.as_view()),
    path('newsletter-api/', views.NewsletterApiView.as_view()),
]
