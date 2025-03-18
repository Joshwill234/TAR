from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home.html'),
    path('', views.signup, name='signup.html'),
    path('', views.blog, name='blog.html'),
    path('', views.login, name='login.html'),
    path('', views.search, name='search.html'),
]