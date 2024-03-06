# Generated by Django 5.0.2 on 2024-03-06 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0031_alter_posts_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='dislike',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='like',
            name='dislike_permi',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='like',
            name='like',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='like',
            name='like_permi',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='posts',
            name='post_dislike',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='posts',
            name='post_like',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]