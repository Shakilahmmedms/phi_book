# Generated by Django 5.0.2 on 2024-03-04 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_posts_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='user',
        ),
    ]