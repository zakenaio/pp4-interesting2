from .forms import NewsPostForm

def news_post_form(request):
    return {'news_post_form': NewsPostForm()}