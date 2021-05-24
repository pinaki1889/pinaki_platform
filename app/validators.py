from django.core.exceptions import ValidationError

def file_size(value):
    filesize = value.size
    if filesize > 4e+8:
        raise ValidationError("maximum size you can upload is 50 mb ")


