from datetime import date

from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone

from .validators import file_size
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Video(models.Model):
    caption = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    video = models.FileField(upload_to="video/%y", validators=[file_size])
    #author = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    likes = models.ManyToManyField(User,related_name="blog_posts1",blank=True)
    verified= models.BooleanField(default=False)

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.caption

"""class Video(models.Model):
    caption = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    video = models.FileField(upload_to="video/%y", validators=[file_size])

    def __str__(self):
        return self.caption"""

class Image(models.Model):
    caption = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="img/%y", validators=[file_size])
    likes = models.ManyToManyField(User, related_name="blog_posts2",blank=True)
    #author = models.ForeignKey(User, on_delete=models.CASCADE,default='contact_default')
    verified = models.BooleanField(default=False)

    def number_of_likes(self):
        return self.likes.count()


    def __str__(self):
        return self.caption


class File(models.Model):
    caption = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to="file/%y", validators=[file_size])
    likes = models.ManyToManyField(User, related_name="blog_posts3",blank=True)
    #author = models.ForeignKey(User, on_delete=models.CASCADE,default='contact_default')
    verified = models.BooleanField(default=False)

    def number_of_likes(self):
        return self.likes.count()


    def __str__(self):
        return self.caption

class Comment1(models.Model):
    post = models.ForeignKey(Video, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField(null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.caption,self.name)


class Comment2(models.Model):
    post = models.ForeignKey(Image, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField(null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.caption,self.name)


class Comment3(models.Model):
    post = models.ForeignKey(File, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField(null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.caption,self.name)