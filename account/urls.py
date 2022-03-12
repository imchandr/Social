import imp
from django.urls import path
from django.contrib.auth import views as auth_views
from account import views as user_views
from account.forms import LoginForm
app_name = 'user'
urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html',authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/landing_page.html'), name='logout'),
]
