from django.contrib import admin
from django import forms
from .models import News_Post, Comment, Category, Profile
from .forms import PostForm, CommentForm 

@admin.register(News_Post)
class PostAdmin(admin.ModelAdmin):
    form = PostForm

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    form = CommentForm
    list_display = ('author_name', 'post', 'pub_date')
    list_filter = ('post', 'pub_date')
    fields = ['post', 'author_name', 'text']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

class PostForm(forms.ModelForm):
    class Meta:
        model = News_Post
        fields = ['title', 'content', 'author']  

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'author_name', 'text'] 

admin.site.register(Profile) 

