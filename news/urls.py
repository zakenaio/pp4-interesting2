from django.urls import path, include
from . import views
from .views import news_list, create_news



urlpatterns = [
    path('', news_list, name='news_list'),
    path('news-details/<slug:slug>/', views.news_details, name='news_details'),
    path('top-posts/', views.top_posts, name='top_posts'),
    path('vote/', views.vote, name='vote'),
    path('create_news/', views.create_news, name='create_news'),
    path('edit_news/<slug:slug>/', views.edit_news, name='edit_news'),
    path('delete_news/<slug:slug>/', views.delete_news, name='delete_news'),
]