from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

from users import views

app_name = 'users'

urlpatterns = [
    path('', views.UserListView.as_view(), name='index'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
