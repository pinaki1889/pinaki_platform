# Generated by Django 3.1.5 on 2021-02-11 04:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0012_auto_20210211_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='author',
            field=models.ForeignKey(default='contact_default', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='image',
            name='author',
            field=models.ForeignKey(default='contact_default', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='video',
            name='author',
            field=models.ForeignKey(default='contact_default', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
