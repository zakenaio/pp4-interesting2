from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import News_Post
from django.apps import apps

Comment = apps.get_model('news', 'Comment')

class PostForm(forms.ModelForm):
    class Meta:
        model = News_Post
        fields = '__all__'
        widgets = {
            'content': CKEditorUploadingWidget(),
        }


class NewsPostForm(forms.ModelForm):
    class Meta:
        model = News_Post
        fields = ['title', 'author', 'content', 'category',]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']  # Exclude the post field