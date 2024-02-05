# news/views.py

from django.shortcuts import render, get_object_or_404
from .models import News_Post

def news_list(request):
    posts = News_Post.objects.all()
    return render(request, 'news_list.html', {'posts': posts})

def news_detail(request, pk):
    post = get_object_or_404(News_Post, pk=pk)
    return render(request, 'news/post_detail.html', {'post': post})