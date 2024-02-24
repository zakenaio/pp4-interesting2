from django.urls import path
from . import views
from .views import news_list, delete_news, edit_news


urlpatterns = [
    path('', news_list, name='news_list'),
    path('news-details/<slug:slug>/', views.news_details, name='news_details'),
    path('top-posts/', views.top_posts, name='top_posts'),
    path('vote/', views.vote, name='vote'),
    path('create_news/', views.create_news, name='create_news'),
    path('edit_news/<slug:slug>/', edit_news, name='edit_news'),
    path('delete_news/<slug:slug>/', delete_news, name='delete_news'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
