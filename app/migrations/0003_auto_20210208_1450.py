# Generated by Django 3.1.5 on 2021-02-08 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_video_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='image',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
