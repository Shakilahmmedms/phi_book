# Generated by Django 5.0.2 on 2024-03-04 12:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_remove_posts_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='post',
        ),
        migrations.AddField(
            model_name='like',
            name='like',
            field=models.OneToOneField(default=None, null=None, on_delete=django.db.models.deletion.CASCADE, to='posts.posts'),
        ),
    ]
