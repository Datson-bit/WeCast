# Generated by Django 3.0 on 2020-09-03 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0008_auto_20200902_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='CText',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='Cname',
        ),
        migrations.AddField(
            model_name='comment',
            name='body',
            field=models.TextField(default=1),
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default=2, max_length=255),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Blogs.Post'),
        ),
    ]
