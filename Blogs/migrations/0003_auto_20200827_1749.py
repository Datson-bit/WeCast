# Generated by Django 3.0 on 2020-08-28 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0002_post_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img_url',
            field=models.CharField(max_length=2083),
        ),
    ]
