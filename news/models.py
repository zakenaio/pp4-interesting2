from django.db import models
from django.utils.text import slugify
from django import forms
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from PIL import Image


class Category(models.Model):
    """
    Represents a category for posts. Each category has a unique name, 
    an optional description, and a publication date.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class News_Post(models.Model):
    """
    Represents a news post. Each post has a title, rich text content, an author,
    an optional category, a publication date, and a vote count.
    """
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True, unique=True)
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            # Ensure the slug is unique
            unique_slug = self.slug
            num = 1
            while News_Post.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{self.slug}-{num}'
                num += 1
            self.slug = unique_slug
        super(News_Post, self).save(*args, **kwargs)


    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Represents a comment on a post. Each comment is linked to a post, may have 
    an author name (if the author is unauthenticated), contains text, and has a 
    publication date.
    """
    post = models.ForeignKey(News_Post, related_name='comments', on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100, blank=False, null=True) 
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Comment by {self.author_name or 'Anonymous'} on {self.post.title}"


class CommentForm(forms.ModelForm):
    """
    A Django form for creating and editing comments.
    """
    class Meta:
        model = Comment
        exclude = ['post']


class Profile(models.Model):
    """
    Represents a user profile. Each profile is linked to a user and has an avatar image.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(
        default='avatar.jpg',
        upload_to='profile_avatars'
    )

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        """
        Saves the profile and resizes the avatar image if it's larger than 300x300 pixels.
        """
        # save the profile first
        super().save(*args, **kwargs)

        # resize the image
        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            # create a thumbnail
            img.thumbnail(output_size)
            # overwrite the larger image
            img.save(self.avatar.path)