# news/views.py

from django.shortcuts import render, get_object_or_404
from .models import News_Post
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .forms import CommentForm

def news_list(request):
    posts = News_Post.objects.all()
    return render(request, 'news_list.html', {'posts': posts})

#def news_detail(request, pk):
#    post = get_object_or_404(News_Post, pk=pk)
#    return render(request, 'post_detail.html', {'post': post})


def news_details(request, post_id):
    post = get_object_or_404(News_Post, pk=post_id)
    comments = post.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            # Redirect or render as necessary
        else:
            # Form is not valid, add a warning message
            messages.warning(request, 'Please fill in all required fields.')
            # Render the form with errors (and messages will be included in the context)
    else:
        form = CommentForm()

    return render(request, 'news_details.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })


@require_POST
def vote(request):
    post_id = request.POST.get('post_id')
    post = Post.objects.get(pk=post_id)

    # Increment the post's vote count and save it
    post.votes += 1
    post.save()

    # Return a JSON response confirming the vote
    return JsonResponse({'message': 'Vote added successfully'})


def top_posts(request):
    top_posts = Post.objects.order_by('-votes')
    return render(request, 'top_posts.html', {'top_posts': top_posts})


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')