# Generated by Django 5.0.2 on 2024-03-05 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0022_rename_like_like_post_posts_created_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/uploads/'),
        ),
    ]
