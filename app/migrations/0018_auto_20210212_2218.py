# Generated by Django 3.1.5 on 2021-02-12 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20210212_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment1',
            name='date_added',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='comment2',
            name='date_added',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='comment3',
            name='date_added',
            field=models.DateField(auto_now=True),
        ),
    ]