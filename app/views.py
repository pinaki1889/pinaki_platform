from audioop import reverse
from pyexpat.errors import messages
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views import View
from django.views.generic import DetailView, CreateView
from django.urls import reverse, reverse_lazy
from pip._vendor.requests import post

from .forms import RegistrationForm, LoginForm, ModelFormWithFileField, CommentForm1, CommentForm2, CommentForm3
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import Video_form
from .models import Video, Comment1,Comment2,Comment3
from .forms import ImageForm
from .models import Image
from .models import File



def index(request):
    return render(request, 'index.html')


def registration(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            #return HttpResponse("<h1>Registration  Successful</h1>")
            #return  redirect("home")
            return render(request, "regsuccess.html")
    else:
        user_form = RegistrationForm()
    return render(request, 'registration.html', {"user_form": user_form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd["username"], password=cd["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("home")
                else:
                    return render(request, "loginwrong.html")
            else:
                return render(request, "loginwrong.html")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
@login_required

def user_logout(request):
    logout(request)
    #return HttpResponse("<h1>Logout Successful</h1>")
    return redirect("home")



def user_image(request):
    if request.method=="GET":
        if 'p' in request.GET:
            p = request.GET['p']
            all_image = Image.objects.filter(name=p)
        else:
            all_image = Image.objects.filter(verified=True)

        for vid in all_image:
            vid.post_is_liked = vid.likes.filter(id=request.user.id).exists()

            # print(vid)
            # print(vid.caption," : ",vid.number_of_likes())
            # print("Liked : ",)
        form = ImageForm()
        #return render(request, 'video.html', {"form": form, "all": all_video})
        return render(request, "image.html", {"form": form, "all": all_image})

    if request.method == "POST":
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            #return HttpResponse("<h1> Uploaded successfully </h1>")
            #return redirect("user_image")
            return render(request, "imagesuccess.html")
    else:
        form = ImageForm()
    #return render(request, 'video.html', {"form": form, "all": all_video})
    return render(request, "image.html", {"form": form, "all": all_image})



def user_video(request):
    if request.method == "GET":
        if 'q' in request.GET:
            q = request.GET['q']
            all_video = Video.objects.filter(name=q)
        else:
            all_video = Video.objects.filter(verified=True)

        for vid in all_video:
            vid.post_is_liked=vid.likes.filter(id=request.user.id).exists()

            # print(vid)
            # print(vid.caption," : ",vid.number_of_likes())
            # print("Liked : ",)
        form = Video_form()
        return render(request, 'video.html', {"form": form, "all": all_video})
    if request.method == "POST":
        form = Video_form(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            #return HttpResponse("<h1> Uploaded successfully </h1>")
            #return redirect("user_video")
            return render(request, "videosuccess.html")
    else:
        form = Video_form()
    #return render(request, 'video.html', {"form": form, "all": all_video})

def user_file(request):
    if request.method=="GET":
        if 'r' in request.GET:
            r = request.GET['r']
            all_file = File.objects.filter(name=r)
        else:
            all_file = File.objects.filter(verified=True)

        for vid in all_file:
            vid.post_is_liked=vid.likes.filter(id=request.user.id).exists()
        form = ModelFormWithFileField()
        return render(request, 'file.html', {'form': form, "all": all_file})

    if request.method == "POST":
        form = ModelFormWithFileField(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            #return HttpResponse("<h1> Uploaded successfully </h1>")
            #return redirect("user_file")
            return render(request, "filesuccess.html")
    else:
        form = ModelFormWithFileField()
    return render(request, 'file.html', {"form": form, "all": all_file})

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

def BlogPostLike1(request, pk):
    post = get_object_or_404(Video, id=request.POST.get('blogpost_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect("/video")

class BlogPostDetailView1(DetailView):
    model = Video
    # template_name = MainApp/BlogPost_detail.html
    # context_object_name = 'object'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Video, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        return data

def BlogPostLike2(request, pk):
    post = get_object_or_404(Image, id=request.POST.get('blogpost_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect("/image")

class BlogPostDetailView2(DetailView):
    model = Image
    # template_name = MainApp/BlogPost_detail.html
    # context_object_name = 'object'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Image, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        return data

def BlogPostLike3(request, pk):
    post = get_object_or_404(File, id=request.POST.get('blogpost_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect("/file")

class BlogPostDetailView3(DetailView):
    model = File
    # template_name = MainApp/BlogPost_detail.html
    # context_object_name = 'object'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(File, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        return data

#video
class AddCommentView1(CreateView):
    model = Comment1
    form_class = CommentForm1
    template_name = 'add_comment1.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('user_video')


#image
class AddCommentView2(CreateView):
    model = Comment2
    form_class = CommentForm2
    template_name = 'add_comment2.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('user_image')

#file
class AddCommentView3(CreateView):
    model = Comment3
    form_class = CommentForm3
    template_name = 'add_comment3.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('user_file')

