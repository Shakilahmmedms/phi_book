# Generated by Django 5.0.2 on 2024-03-08 10:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0038_like_dislike_like_dislike_permi_like_like_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='post_dislike',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='post_like',
        ),
        migrations.AddField(
            model_name='posts',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]