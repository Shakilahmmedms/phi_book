# Generated by Django 5.0.2 on 2024-03-04 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_useraccounts_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccounts',
            name='like_history',
        ),
    ]
