from django.contrib import admin

# Register your models here.
from .models import Video, Comment1, Comment2, Comment3

from .models import Image

from .models import File


from django.contrib import admin


admin.site.register(Video)

admin.site.register(Image)

admin.site.register(File)

admin.site.register(Comment1)

admin.site.register(Comment2)

admin.site.register(Comment3)