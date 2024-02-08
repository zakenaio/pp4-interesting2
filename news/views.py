from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import News_Post
from .forms import CommentForm
from .forms import NewsPostForm



def news_list(request):
    post_form_pairs = [(post, NewsPostForm(instance=post)) for post in News_Post.objects.order_by('-pub_date')]
    return render(request, 'news_list.html', {'post_form_pairs': post_form_pairs})


def news_details(request, slug):
    post = get_object_or_404(News_Post, slug=slug)
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


def create_news(request):
    if request.method == 'POST':
        form = NewsPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    # Handle non-POST requests or invalid form submissions
    return JsonResponse({'error': "Invalid request"}, status=400)


@login_required
def edit_news(request, slug):
    post = get_object_or_404(News_Post, slug=slug)
    if request.method == 'POST':
        form = NewsPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('news_list')  
    else:
        form = NewsPostForm(instance=post)
    return render(request, 'news_list.html', {'form': form})

@require_POST
@login_required
def delete_news(slug):
    post = get_object_or_404(News_Post, slug=slug)
    post.delete()
    return redirect('news_list')


@require_POST
def vote(request):
    post_slug = request.POST.get('slug')  
    post = get_object_or_404(News_Post, slug=post_slug) 

    # Increment the post's vote count and save it
    post.votes += 1
    post.save()

    # Return a JSON response confirming the vote
    return JsonResponse({'votes': post.votes})


def top_posts(request):
    top_posts = News_Post.objects.order_by('-votes')
    return render(request, 'top_posts.html', {'top_posts': top_posts})


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')