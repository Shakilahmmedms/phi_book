# Generated by Django 5.0.2 on 2024-03-05 03:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_rename_buy_date_like_like_date_remove_like_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='like',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.posts'),
        ),
    ]
