# Generated by Django 4.1 on 2024-02-09 14:11

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='news_post',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
