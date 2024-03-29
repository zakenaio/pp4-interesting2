# Generated by Django 4.1 on 2024-02-12 15:12

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_alter_news_post_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_post',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
