from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import News_Post, Comment
# Ensure you're importing the correct Comment model

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
    
    def __init__(self, *args, **kwargs):
        prefix = kwargs.get('prefix', '')
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['id'] = f'{prefix}_id_title'
        self.fields['author'].widget.attrs['id'] = f'{prefix}_id_author'
        self.fields['content'].widget.attrs['id'] = f'{prefix}_id_content'
        self.fields['category'].widget.attrs['id'] = f'{prefix}_id_category'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']