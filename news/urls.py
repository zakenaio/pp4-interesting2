from django.urls import path
from .views import news_list, news_detail  # Ensure post_detail is imported

urlpatterns = [
    path('', news_list, name='news_list'),
    path('news/<int:pk>/', news_detail, name='news_detail'),  # Add this line
]