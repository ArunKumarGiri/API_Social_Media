# Generated by Django 4.0.2 on 2022-02-28 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smapps', '0003_rename_likes_like_liked_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='comment',
        ),
        migrations.AddField(
            model_name='comments',
            name='comment_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
