# Generated by Django 3.0 on 2020-08-31 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0004_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='img_url',
        ),
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default=2, upload_to=''),
        ),
    ]
