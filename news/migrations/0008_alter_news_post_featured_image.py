# Generated by Django 4.1 on 2024-02-12 15:13

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_alter_news_post_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_post',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(blank=True, default=None, max_length=255, null=True, verbose_name='image'),
        ),
    ]