# Generated by Django 5.0.2 on 2024-03-05 03:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0016_alter_like_like'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='like_history',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='like_history', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]