from django.urls import path, include
from .import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="home"),
    path('registration/', views.registration, name="reg"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('video/', views.user_video, name="user_video"),
    path('image/', views.user_image, name="user_image"),
    path('file/', views.user_file, name="user_file"),
    path('blogpost-like1/<int:pk>', views.BlogPostLike1, name="blogpost_like1"),
    path('blogpost-like2/<int:pk>', views.BlogPostLike2, name="blogpost_like2"),
    path('blogpost-like3/<int:pk>', views.BlogPostLike3, name="blogpost_like3"),
    path('video/<int:pk>/comment1/', views.AddCommentView1.as_view(), name="add_comment1"),
    path('image/<int:pk>/comment2/', views.AddCommentView2.as_view(), name="add_comment2"),
    path('file/<int:pk>/comment3/', views.AddCommentView3.as_view(), name="add_comment3"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = "reset_password.html"), name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "password_reset_sent.html"), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "password_reset_form.html"), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "password_reset_done.html"), name ='password_reset_complete')

]
