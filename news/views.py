# Django
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

# Local Django
from .forms import CommentForm, NewsPostForm
from .models import News_Post, Comment


def news_list(request):
    post_form_pairs = [
        (post, NewsPostForm(instance=post, prefix=f'form_{post.slug}'))
        for post in News_Post.objects.order_by('-pub_date')
    ]
    return render(request, 'news_list.html', {'post_form_pairs': post_form_pairs})


def news_details(request, slug):
    post = get_object_or_404(News_Post, slug=slug)
    comments = post.comments.all()
    post_form = NewsPostForm(instance=post, prefix='post')
    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'Your comment has been added.')
            return redirect('news_details', slug=slug)
        else:
            messages.error(request, 'There was an error with your comment.')
            return redirect('news_details', slug=slug)

    comment_form = CommentForm()
    template = 'news_details.html'
    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'post_form': post_form,
    }
    return render(request, template, context)


@login_required
def create_news(request):
    if request.method == 'POST':
        form = NewsPostForm(request.POST, request.FILES)
        if form.is_valid():
            news_post = form.save(commit=False)
            news_post.author = request.user
            news_post.save()
            return redirect('news_details', slug=news_post.slug)
    return JsonResponse({'error': "Invalid request"}, status=400)


@login_required
def edit_news(request, slug):
    post = get_object_or_404(News_Post, slug=slug)
    if post.author != request.user:
        messages.error(request, 'Access denied, this is not your news post.')
        return redirect('news_details', slug=slug)

    if request.method == 'POST':
        form = NewsPostForm(request.POST, request.FILES, instance=post, prefix='post')
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully.')
            return redirect('news_details', slug=slug)
        messages.error(request, 'Error: please try again')

    return redirect('news_details', slug=slug)


@require_POST
@login_required
def delete_news(request, slug):
    post = get_object_or_404(News_Post, slug=slug)
    if post.author != request.user:
        messages.error(request, 'Access denied, this is not your news post.')
        return redirect('news_details', slug=slug)

    post.delete()
    messages.success(request, 'New post successfully deleted!')
    return redirect('news_list')


@require_POST
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if not request.user.is_superuser:
        messages.error(request, 'Only admins can perform this action')
        return redirect('news_details', slug=comment.post.slug)

    comment.delete()
    messages.success(request, "Comment deleted successfully.")
    return redirect('news_details', slug=comment.post.slug)


@require_POST
def vote(request):
    post_slug = request.POST.get('slug')
    post = get_object_or_404(News_Post, slug=post_slug)

    # Increment the post's vote count and save it
    post.votes += 1
    post.save()

    return JsonResponse({'votes': post.votes})


def top_posts(request):
    top_posts = News_Post.objects.order_by('-votes')
    return render(request, 'top_posts.html', {'top_posts': top_posts})


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
