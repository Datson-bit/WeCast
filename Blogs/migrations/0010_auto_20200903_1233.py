# Generated by Django 3.0 on 2020-09-03 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0009_auto_20200902_1700'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='comment',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='sport',
            name='like',
        ),
    ]