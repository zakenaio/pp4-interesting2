from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import News_Post, Comment


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
        fields = ['title', 'content', 'category', 'featured_image']

    def __init__(self, *args, **kwargs):
        prefix = kwargs.get('prefix', '')
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['id'] = f'{prefix}_id_title'
        self.fields['content'].widget.attrs['id'] = f'{prefix}_id_content'
        self.fields['category'].widget.attrs['id'] = f'{prefix}_id_category'
        self.fields['featured_image'].widget.attrs['id'] = f'{prefix}_featured_image'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
