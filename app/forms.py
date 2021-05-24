from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from .models import Video, Comment1,Comment2,Comment3
from .models import Image
from .models import File

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class Video_form(forms.ModelForm):
    class Meta:
        model = Video
        fields = ("caption", "name", "video")
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ("caption", "name", "image")

class ModelFormWithFileField(forms.ModelForm):
    class Meta:
        model = File
        fields = ("caption", "name", "file")


#video
class CommentForm1(forms.ModelForm):
    class Meta:
        model = Comment1
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
#image

class CommentForm2(forms.ModelForm):
    class Meta:
        model = Comment2
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
#file
class CommentForm3(forms.ModelForm):
    class Meta:
        model = Comment3
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }