# Generated by Django 3.1.5 on 2021-02-12 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_remove_video_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment1',
            name='date_added',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment2',
            name='date_added',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment3',
            name='date_added',
            field=models.DateField(auto_now_add=True),
        ),
    ]