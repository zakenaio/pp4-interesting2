from django.urls import path
from . import views
from .views import news_list, news_details, top_posts


urlpatterns = [
    path('', news_list, name='news_list'),
    path('news-details/<slug:slug>/', views.news_details, name='news_details'),
    path('top-posts/', views.top_posts, name='top_posts'),
    path('vote/', views.vote, name='vote'),
]